from eval_harness.metrics import hit_rate, precision_at_k, recall_at_k


def test_recall_at_k_partial_overlap():
    relevant = ["a", "b", "c"]
    ranked = ["a", "x", "b", "y"]
    assert recall_at_k(relevant, ranked, k=3) == 2 / 3


def test_precision_at_k_counts_top_hits():
    relevant = ["a", "b"]
    ranked = ["a", "x", "b"]
    assert precision_at_k(relevant, ranked, k=2) == 0.5


def test_hit_rate_positive():
    assert hit_rate(["a"], ["x", "a", "y"], k=2) == 1.0


def test_hit_rate_miss():
    assert hit_rate(["a"], ["x", "y", "z"], k=2) == 0.0
