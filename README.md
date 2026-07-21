# eval-harness

Offline evaluation harness for retrieval and agent quality gates.

Use this package to score ranked retrieval outputs against golden fixtures and to fail CI when quality drops below a configured threshold.

## Install

```bash
pip install -e ".[dev]"
```

Or install runtime dependencies only:

```bash
pip install -e .
```

## Run tests

```bash
pytest
```

## Quick start

```python
from eval_harness.runner import run_evaluation
from eval_harness.report import format_report

results = run_evaluation("fixtures/golden/sample.json")
print(format_report(results))
```

## Metrics

- `recall_at_k` - fraction of relevant items recovered in the top-k ranks
- `precision_at_k` - fraction of the top-k ranks that are relevant
- `hit_rate` - whether at least one relevant item appears in the top-k ranks

## Layout

- `src/eval_harness/` - metrics runner and reporting
- `fixtures/golden/` - small golden datasets
- `tests/` - pytest coverage for metrics and the runner
## Regression gate

Fail CI when aggregate quality drops below a threshold:

```bash
eval-harness --fixture fixtures/golden/sample.json --k 3 --min-recall 0.5 --min-precision 0.3 --min-hit-rate 0.5
```

The command exits non-zero when any configured minimum is not met.
