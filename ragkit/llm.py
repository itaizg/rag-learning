"""
Unified LLM interface: generate() works identically for Claude and Ollama.

Usage
-----
from ragkit.llm import generate, generate_tools

# Text generation
response = generate("What is RAG?")

# Vision (pass PIL images or file paths)
response = generate("Describe this image", images=["path/to/img.png"])

# Tool calling (for agentic notebooks)
result = generate_tools(prompt, tools=[...])
"""
from __future__ import annotations

import base64
import json
import os
from pathlib import Path
from typing import Any

from ragkit.config import (
    BACKEND,
    CLAUDE_TEXT_MODEL,
    CLAUDE_VISION_MODEL,
    OLLAMA_HOST,
    OLLAMA_TEXT_MODEL,
    OLLAMA_VISION_MODEL,
)


# ── helpers ───────────────────────────────────────────────────────────────────

def _img_to_b64(img) -> tuple[str, str]:
    """Return (base64_data, media_type) from a path, bytes, or PIL image."""
    from PIL import Image
    import io

    if isinstance(img, (str, Path)):
        path = Path(img)
        with open(path, "rb") as f:
            data = f.read()
        media_type = {
            ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".png": "image/png", ".gif": "image/gif", ".webp": "image/webp",
        }.get(path.suffix.lower(), "image/png")
    elif isinstance(img, bytes):
        data = img
        media_type = "image/png"
    else:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        data = buf.getvalue()
        media_type = "image/png"

    return base64.standard_b64encode(data).decode(), media_type


# ── Claude backend ────────────────────────────────────────────────────────────

def _claude_generate(
    prompt: str,
    system: str = "You are a helpful assistant.",
    images: list | None = None,
    max_tokens: int = 1024,
) -> str:
    import anthropic

    client = anthropic.Anthropic()
    model = CLAUDE_VISION_MODEL if images else CLAUDE_TEXT_MODEL

    content: list[dict] = []
    if images:
        for img in images:
            b64, mime = _img_to_b64(img)
            content.append({
                "type": "image",
                "source": {"type": "base64", "media_type": mime, "data": b64},
            })
    content.append({"type": "text", "text": prompt})

    msg = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": content}],
    )
    return msg.content[0].text


def _claude_generate_tools(
    prompt: str,
    tools: list[dict],
    system: str = "You are a helpful assistant.",
    max_tokens: int = 2048,
) -> dict:
    """Returns {"tool_calls": [...], "text": "..."} or {"text": "..."}."""
    import anthropic

    client = anthropic.Anthropic()

    # Convert OpenAI-style tools to Anthropic format if needed
    anthropic_tools = []
    for t in tools:
        if "function" in t:          # OpenAI wrapper format
            fn = t["function"]
            anthropic_tools.append({
                "name": fn["name"],
                "description": fn.get("description", ""),
                "input_schema": fn.get("parameters", {"type": "object", "properties": {}}),
            })
        else:                        # already Anthropic format
            anthropic_tools.append(t)

    msg = client.messages.create(
        model=CLAUDE_TEXT_MODEL,
        max_tokens=max_tokens,
        system=system,
        tools=anthropic_tools,
        messages=[{"role": "user", "content": prompt}],
    )

    tool_calls = [
        {"name": b.name, "input": b.input}
        for b in msg.content
        if b.type == "tool_use"
    ]
    text = " ".join(b.text for b in msg.content if b.type == "text")
    return {"tool_calls": tool_calls, "text": text, "stop_reason": msg.stop_reason}


# ── Ollama backend ────────────────────────────────────────────────────────────

def _ollama_generate(
    prompt: str,
    system: str = "You are a helpful assistant.",
    images: list | None = None,
    max_tokens: int = 1024,
) -> str:
    import ollama as _ollama

    model = OLLAMA_VISION_MODEL if images else OLLAMA_TEXT_MODEL
    msgs: list[dict] = [{"role": "system", "content": system}]

    if images:
        # Ollama vision: pass raw bytes
        img_bytes = []
        for img in images:
            if isinstance(img, (str, Path)):
                img_bytes.append(Path(img).read_bytes())
            elif hasattr(img, "tobytes"):
                import io
                buf = io.BytesIO()
                img.save(buf, format="PNG")
                img_bytes.append(buf.getvalue())
            else:
                img_bytes.append(img)
        msgs.append({"role": "user", "content": prompt, "images": img_bytes})
    else:
        msgs.append({"role": "user", "content": prompt})

    resp = _ollama.chat(model=model, messages=msgs, options={"num_predict": max_tokens})
    return resp.message.content


def _ollama_generate_tools(
    prompt: str,
    tools: list[dict],
    system: str = "You are a helpful assistant.",
    max_tokens: int = 2048,
) -> dict:
    """
    Try native Ollama tool-calling; fall back to a JSON-decision prompt
    for models that don't support it.
    """
    import ollama as _ollama

    # Normalize tools to OpenAI format (what Ollama expects)
    ollama_tools = []
    for t in tools:
        if "function" in t:
            ollama_tools.append(t)
        else:
            ollama_tools.append({
                "type": "function",
                "function": {
                    "name": t["name"],
                    "description": t.get("description", ""),
                    "parameters": t.get("input_schema", {"type": "object", "properties": {}}),
                },
            })

    msgs = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt},
    ]

    try:
        resp = _ollama.chat(
            model=OLLAMA_TEXT_MODEL,
            messages=msgs,
            tools=ollama_tools,
            options={"num_predict": max_tokens},
        )
        calls = []
        if resp.message.tool_calls:
            for tc in resp.message.tool_calls:
                calls.append({"name": tc.function.name, "input": tc.function.arguments})
        return {"tool_calls": calls, "text": resp.message.content or "", "stop_reason": "tool_use" if calls else "end_turn"}
    except Exception:
        # Fallback: ask the model to respond with JSON
        tool_desc = json.dumps([t.get("function", t) for t in ollama_tools], indent=2)
        fallback_prompt = (
            f"{prompt}\n\n"
            f"You have access to these tools:\n{tool_desc}\n\n"
            "If you need to call a tool, respond with ONLY valid JSON in this exact format:\n"
            '{"tool": "<name>", "args": {<arguments>}}\n'
            "Otherwise respond normally with text."
        )
        raw = _ollama_generate(fallback_prompt, system=system, max_tokens=max_tokens)
        try:
            parsed = json.loads(raw.strip())
            if "tool" in parsed:
                return {
                    "tool_calls": [{"name": parsed["tool"], "input": parsed.get("args", {})}],
                    "text": "",
                    "stop_reason": "tool_use",
                }
        except (json.JSONDecodeError, KeyError):
            pass
        return {"tool_calls": [], "text": raw, "stop_reason": "end_turn"}


# ── Public API ────────────────────────────────────────────────────────────────

def generate(
    prompt: str,
    system: str = "You are a helpful assistant.",
    images: list | None = None,
    max_tokens: int = 1024,
    backend: str | None = None,
) -> str:
    """Generate a text response. backend defaults to ragkit.config.BACKEND."""
    bk = backend or BACKEND
    if bk == "claude":
        return _claude_generate(prompt, system=system, images=images, max_tokens=max_tokens)
    return _ollama_generate(prompt, system=system, images=images, max_tokens=max_tokens)


def generate_tools(
    prompt: str,
    tools: list[dict],
    system: str = "You are a helpful assistant.",
    max_tokens: int = 2048,
    backend: str | None = None,
) -> dict:
    """Generate with tool-calling support. Returns {"tool_calls", "text", "stop_reason"}."""
    bk = backend or BACKEND
    if bk == "claude":
        return _claude_generate_tools(prompt, tools, system=system, max_tokens=max_tokens)
    return _ollama_generate_tools(prompt, tools, system=system, max_tokens=max_tokens)
