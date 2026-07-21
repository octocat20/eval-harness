"""Format evaluation results for humans and CI logs."""

from __future__ import annotations

from typing import Any, Dict


def format_report(results: Dict[str, Any]) -> str:
    """Render a compact text report from runner output."""
    k = results.get("k", "?")
    aggregates = results.get("aggregates", {})
    lines = [
        f"Evaluation report (k={k})",
        f"  recall_at_k:    {aggregates.get('recall_at_k', 0.0):.4f}",
        f"  precision_at_k: {aggregates.get('precision_at_k', 0.0):.4f}",
        f"  hit_rate:       {aggregates.get('hit_rate', 0.0):.4f}",
        "Cases:",
    ]
    for case in results.get("cases", []):
        lines.append(
            "  - {id}: recall_at_k={recall:.4f} precision_at_k={precision:.4f} hit_rate={hit:.4f}".format(
                id=case.get("id"),
                recall=case.get("recall_at_k", 0.0),
                precision=case.get("precision_at_k", 0.0),
                hit=case.get("hit_rate", 0.0),
            )
        )
    return "\n".join(lines)
