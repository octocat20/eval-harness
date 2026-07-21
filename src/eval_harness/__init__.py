"""Offline evaluation harness for retrieval and agent quality gates."""

__version__ = "0.1.0"

from eval_harness.metrics import hit_rate, recall_at_k
from eval_harness.report import format_report
from eval_harness.runner import run_evaluation

__all__ = [
    "__version__",
    "hit_rate",
    "recall_at_k",
    "format_report",
    "run_evaluation",
]
