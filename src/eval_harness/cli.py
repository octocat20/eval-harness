"""Regression gate CLI for offline evaluation thresholds."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from eval_harness.report import format_report
from eval_harness.runner import run_evaluation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="eval-harness",
        description="Run offline retrieval evaluation and enforce a quality gate.",
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        required=True,
        help="Path to a golden fixture JSON file.",
    )
    parser.add_argument("--k", type=int, default=5, help="Cutoff for ranked metrics.")
    parser.add_argument(
        "--min-recall",
        type=float,
        default=0.0,
        help="Minimum aggregate recall_at_k required to pass.",
    )
    parser.add_argument(
        "--min-precision",
        type=float,
        default=0.0,
        help="Minimum aggregate precision_at_k required to pass.",
    )
    parser.add_argument(
        "--min-hit-rate",
        type=float,
        default=0.0,
        help="Minimum aggregate hit_rate required to pass.",
    )
    return parser


def evaluate_gate(results: dict, min_recall: float, min_precision: float, min_hit_rate: float) -> bool:
    aggregates = results.get("aggregates", {})
    return (
        aggregates.get("recall_at_k", 0.0) >= min_recall
        and aggregates.get("precision_at_k", 0.0) >= min_precision
        and aggregates.get("hit_rate", 0.0) >= min_hit_rate
    )


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    results = run_evaluation(args.fixture, k=args.k)
    print(format_report(results))
    passed = evaluate_gate(
        results,
        min_recall=args.min_recall,
        min_precision=args.min_precision,
        min_hit_rate=args.min_hit_rate,
    )
    if not passed:
        print("Regression gate failed: aggregate metrics below configured thresholds.", file=sys.stderr)
        return 1
    print("Regression gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
