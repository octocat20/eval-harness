from pathlib import Path

from eval_harness.cli import evaluate_gate, main
from eval_harness.runner import run_evaluation


FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "golden" / "sample.json"


def test_evaluate_gate_passes_when_above_threshold():
    results = run_evaluation(FIXTURE, k=3)
    assert evaluate_gate(results, min_recall=0.0, min_precision=0.0, min_hit_rate=0.0) is True


def test_evaluate_gate_fails_when_below_threshold():
    results = run_evaluation(FIXTURE, k=3)
    assert evaluate_gate(results, min_recall=1.1, min_precision=0.0, min_hit_rate=0.0) is False


def test_main_exits_nonzero_on_failed_gate(capsys):
    code = main(["--fixture", str(FIXTURE), "--k", "3", "--min-recall", "1.1"])
    assert code == 1
    err = capsys.readouterr().err
    assert "Regression gate failed" in err
