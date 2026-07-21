"""Run evaluation over golden fixtures."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from eval_harness.metrics import hit_rate, recall_at_k


def load_fixture(path: str | Path) -> List[Dict[str, Any]]:
    fixture_path = Path(path)
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("fixture must be a JSON list of cases")
    return payload


def run_evaluation(fixture_path: str | Path, k: int = 5) -> Dict[str, Any]:
    """Score each fixture case and return aggregate metrics."""
    cases = load_fixture(fixture_path)
    if not cases:
        return {"cases": [], "aggregates": {"recall_at_k": 0.0, "hit_rate": 0.0}, "k": k}

    scored: List[Dict[str, Any]] = []
    recall_scores: List[float] = []
    hit_scores: List[float] = []

    for case in cases:
        case_id = str(case.get("id", len(scored)))
        relevant = case.get("relevant", [])
        ranked = case.get("ranked", [])
        recall = recall_at_k(relevant, ranked, k)
        hit = hit_rate(relevant, ranked, k)
        scored.append(
            {
                "id": case_id,
                "recall_at_k": recall,
                "hit_rate": hit,
            }
        )
        recall_scores.append(recall)
        hit_scores.append(hit)

    aggregates = {
        "recall_at_k": sum(recall_scores) / len(recall_scores),
        "hit_rate": sum(hit_scores) / len(hit_scores),
    }
    return {"cases": scored, "aggregates": aggregates, "k": k}
