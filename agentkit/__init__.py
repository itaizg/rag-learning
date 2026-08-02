"""agentkit — small production-pattern primitives for the agent notebooks
(tool contracts, semantic caching, multi-tenant isolation).

A teaching package, not a framework: each module is under 200 lines and
meant to be read end-to-end, the same way ragkit is for retrieval.
"""

from agentkit.contracts import ToolContract, ToolResult, checked_execute, contracts_from_schemas, detect_bad_call, validate_args
from agentkit.semcache import CacheHit, SemanticCache
from agentkit.tenancy import CostLedger, NamespacedStore, TenantContext

__all__ = [
    "ToolContract",
    "ToolResult",
    "checked_execute",
    "contracts_from_schemas",
    "detect_bad_call",
    "validate_args",
    "CacheHit",
    "SemanticCache",
    "CostLedger",
    "NamespacedStore",
    "TenantContext",
]
