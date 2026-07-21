from pathlib import Path

from eval_harness.report import format_report
from eval_harness.runner import run_evaluation


FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "golden" / "sample.json"


def test_run_evaluation_aggregates():
    results = run_evaluation(FIXTURE, k=3)
    assert results["k"] == 3
    assert len(results["cases"]) == 2
    assert 0.0 <= results["aggregates"]["recall_at_k"] <= 1.0
    assert 0.0 <= results["aggregates"]["hit_rate"] <= 1.0


def test_format_report_contains_metrics():
    results = run_evaluation(FIXTURE, k=3)
    report = format_report(results)
    assert "recall_at_k" in report
    assert "hit_rate" in report
