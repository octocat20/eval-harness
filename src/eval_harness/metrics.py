"""Basic retrieval metrics for offline evaluation."""

from __future__ import annotations

from typing import Iterable, Sequence, Set


def _as_set(items: Iterable[str]) -> Set[str]:
    return {str(item) for item in items}


def recall_at_k(relevant: Sequence[str], ranked: Sequence[str], k: int) -> float:
    """Return the fraction of relevant items found in the top-k ranks."""
    if k <= 0:
        raise ValueError("k must be positive")
    truth = _as_set(relevant)
    if not truth:
        return 0.0
    top = _as_set(ranked[:k])
    return len(truth & top) / len(truth)


def precision_at_k(relevant: Sequence[str], ranked: Sequence[str], k: int) -> float:
    """Return the fraction of the top-k ranks that are relevant."""
    if k <= 0:
        raise ValueError("k must be positive")
    top = ranked[:k]
    if not top:
        return 0.0
    truth = _as_set(relevant)
    hits = sum(1 for item in top if str(item) in truth)
    return hits / len(top)


def hit_rate(relevant: Sequence[str], ranked: Sequence[str], k: int) -> float:
    """Return 1.0 if any relevant item appears in the top-k ranks else 0.0."""
    if k <= 0:
        raise ValueError("k must be positive")
    truth = _as_set(relevant)
    if not truth:
        return 0.0
    top = _as_set(ranked[:k])
    return 1.0 if truth & top else 0.0
