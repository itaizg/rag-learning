"""
Notebook display helpers — rich-formatted output for hits, prompts, and pipelines.
"""
from __future__ import annotations

from ragkit.vectorstore import Hit


def show_hits(hits: list[Hit], max_chars: int = 200, title: str = "Retrieved Chunks") -> None:
    """Pretty-print a list of Hit objects using rich."""
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text

    console = Console()
    table = Table(title=title, show_lines=True, highlight=True)
    table.add_column("Rank", style="bold cyan", width=5)
    table.add_column("Score", style="bold green", width=7)
    table.add_column("Source", style="yellow", width=20)
    table.add_column("Text", style="white")

    for h in hits:
        snippet = h.text[:max_chars] + ("…" if len(h.text) > max_chars else "")
        table.add_row(
            str(h.rank),
            f"{h.score:.3f}",
            h.metadata.get("source", "?"),
            snippet,
        )
    console.print(table)


def show_prompt(prompt: str, title: str = "Prompt sent to LLM") -> None:
    """Display the final prompt with syntax highlighting."""
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
    console.print(Panel(prompt, title=f"[bold blue]{title}[/]", border_style="blue"))


def show_answer(answer: str, title: str = "LLM Answer") -> None:
    """Display the LLM answer."""
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
    console.print(Panel(answer, title=f"[bold green]{title}[/]", border_style="green"))


def show_pipeline_step(step: str, detail: str = "") -> None:
    """Print a pipeline step header."""
    from rich.console import Console
    console = Console()
    line = f"[bold magenta]▶ {step}[/]"
    if detail:
        line += f"  [dim]{detail}[/]"
    console.print(line)


def compare_rankings(
    before: list[Hit],
    after: list[Hit],
    title_before: str = "Before Rerank",
    title_after: str = "After Rerank",
    max_chars: int = 120,
) -> None:
    """Side-by-side comparison of two ranked lists."""
    from rich.console import Console
    from rich.columns import Columns
    from rich.panel import Panel

    console = Console()
    rows_before, rows_after = [], []

    n = max(len(before), len(after))
    for i in range(n):
        if i < len(before):
            h = before[i]
            rows_before.append(f"[cyan]{h.rank}[/] [{h.score:.3f}] {h.text[:max_chars]}")
        if i < len(after):
            h = after[i]
            rows_after.append(f"[cyan]{h.rank}[/] [{h.score:.3f}] {h.text[:max_chars]}")

    console.print(Columns([
        Panel("\n\n".join(rows_before), title=f"[yellow]{title_before}[/]"),
        Panel("\n\n".join(rows_after),  title=f"[green]{title_after}[/]"),
    ]))


def show_graph_context(
    vector_hits: list[Hit],
    graph_context: list[str],
    max_chars: int = 150,
) -> None:
    """Show the two streams of context used in Graph RAG."""
    from rich.console import Console
    from rich.table import Table

    console = Console()

    # Vector context
    vt = Table(title="[yellow]Vector Context[/]", show_lines=True)
    vt.add_column("Rank", width=5)
    vt.add_column("Score", width=7)
    vt.add_column("Text")
    for h in vector_hits:
        vt.add_row(str(h.rank), f"{h.score:.3f}", h.text[:max_chars])
    console.print(vt)

    # Graph context
    gt = Table(title="[green]Graph Traversal Context[/]", show_lines=True)
    gt.add_column("#", width=4)
    gt.add_column("Fact")
    for i, fact in enumerate(graph_context, 1):
        gt.add_row(str(i), fact[:max_chars])
    console.print(gt)


def show_agent_decision(decision: dict) -> None:
    """Display a router agent's tool call decision."""
    from rich.console import Console
    from rich.panel import Panel
    import json

    console = Console()
    if decision.get("tool_calls"):
        calls = decision["tool_calls"]
        body = json.dumps(calls, indent=2)
        console.print(Panel(body, title="[bold magenta]Agent Tool Call[/]", border_style="magenta"))
    else:
        console.print(Panel(decision.get("text", ""), title="[bold cyan]Agent Direct Answer[/]", border_style="cyan"))
