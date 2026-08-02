"""Tool-call reliability primitives: validate arguments, detect hallucinated tool
names, retry with idempotency, and fall back — a small hardening layer over the
nb19-style {TOOL_SCHEMAS, TOOL_IMPLEMENTATIONS} registry shape.

Taught in 04_agents' tool-contracts notebook; reused (via pre_hooks) for
per-tenant budget gating in the multi-tenant isolation notebook.
"""

from __future__ import annotations

import difflib
from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class ToolContract:
    name: str
    input_schema: dict
    validator: Callable[[dict], list[str]] | None = None
    idempotency_key_fn: Callable[[dict], str] | None = None
    fallback: Callable[..., str] | None = None
    max_retries: int = 1
    side_effects: bool = False


@dataclass
class ToolResult:
    status: str  # "ok" | "rejected" | "replayed" | "fallback" | "error"
    output: str
    errors: list[str] = field(default_factory=list)
    attempts: int = 1


def contracts_from_schemas(schemas: list[dict], **overrides: dict) -> dict[str, ToolContract]:
    """Lift an nb19-style TOOL_SCHEMAS list into ToolContract objects.

    `overrides` maps a tool name to extra ToolContract kwargs (validator,
    idempotency_key_fn, fallback, max_retries, side_effects) not present in
    the raw JSON schema.
    """
    contracts = {}
    for schema in schemas:
        name = schema["name"]
        kwargs = dict(overrides.get(name, {}))
        contracts[name] = ToolContract(name=name, input_schema=schema["input_schema"], **kwargs)
    return contracts


def validate_args(contract: ToolContract, args: dict) -> list[str]:
    """Hand-rolled schema check (no jsonschema dependency — the point is to
    read every line): unknown keys, missing required keys, wrong JSON type.
    Then runs the contract's own semantic validator, if any.
    """
    errors: list[str] = []
    schema = contract.input_schema
    properties = schema.get("properties", {})
    required = schema.get("required", [])

    unknown = set(args) - set(properties)
    for key in sorted(unknown):
        errors.append(f"unexpected argument '{key}'")

    for key in required:
        if key not in args:
            errors.append(f"missing required argument '{key}'")

    json_to_python = {
        "string": str,
        "number": (int, float),
        "integer": int,
        "boolean": bool,
        "object": dict,
        "array": list,
    }
    for key, value in args.items():
        prop = properties.get(key)
        if prop is None:
            continue
        expected = json_to_python.get(prop.get("type"))
        if expected is not None and not isinstance(value, expected):
            errors.append(
                f"argument '{key}' should be {prop['type']}, got {type(value).__name__}"
            )

    if contract.validator is not None:
        errors.extend(contract.validator(args))

    return errors


def detect_bad_call(name: str, args: dict, contracts: dict[str, ToolContract]) -> str | None:
    """Return a model-facing error string for a hallucinated tool name or
    invalid arguments, or None if the call is well-formed. This string is
    meant to be fed back as tool_result content so the model can recover.
    """
    if name not in contracts:
        suggestion = difflib.get_close_matches(name, contracts.keys(), n=1)
        if suggestion:
            return f"error: unknown tool '{name}' (did you mean '{suggestion[0]}'?)"
        return f"error: unknown tool '{name}' — no tool with that name is registered"

    errors = validate_args(contracts[name], args)
    if errors:
        return "error: invalid arguments — " + "; ".join(errors)
    return None


def checked_execute(
    name: str,
    args: dict,
    contracts: dict[str, ToolContract],
    implementations: dict[str, Callable[..., str]],
    ledger: dict[str, str] | None = None,
    pre_hooks: list[Callable[[str, dict], str | None]] | None = None,
) -> ToolResult:
    """Execute a tool call with validation, idempotency, retries, and a
    fallback — the hardened replacement for `implementations[name](**args)`.

    Order: pre_hooks (e.g. a tenant budget gate) -> hallucinated-call /
    argument validation -> idempotency-ledger lookup (a hit replays the
    recorded output without re-executing) -> the real implementation with
    retries -> fallback -> error.
    """
    for hook in pre_hooks or []:
        rejection = hook(name, args)
        if rejection is not None:
            return ToolResult(status="rejected", output=rejection, errors=[rejection])

    bad_call = detect_bad_call(name, args, contracts)
    if bad_call is not None:
        return ToolResult(status="rejected", output=bad_call, errors=[bad_call])

    contract = contracts[name]
    ledger = {} if ledger is None else ledger
    idem_key = None
    if contract.idempotency_key_fn is not None:
        idem_key = contract.idempotency_key_fn(args)
        if idem_key in ledger:
            return ToolResult(status="replayed", output=ledger[idem_key])

    impl = implementations[name]
    errors: list[str] = []
    for attempt in range(1, contract.max_retries + 1):
        try:
            output = impl(**args)
            if idem_key is not None:
                ledger[idem_key] = output
            return ToolResult(status="ok", output=output, attempts=attempt)
        except Exception as exc:  # noqa: BLE001 - deliberately broad: any tool failure is retryable
            errors.append(f"attempt {attempt}: {exc!r}")

    if contract.fallback is not None:
        try:
            output = contract.fallback(**args)
            return ToolResult(status="fallback", output=output, errors=errors, attempts=contract.max_retries)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"fallback failed: {exc!r}")

    return ToolResult(status="error", output="error: tool failed after retries", errors=errors, attempts=contract.max_retries)
