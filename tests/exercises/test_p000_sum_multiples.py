import pytest

from exercises.p000_sum_multiples import sum_multiples


def test_sums_multiples_of_three_or_five() -> None:
    assert sum_multiples(10, (3, 5)) == 23


def test_does_not_count_shared_multiples_twice() -> None:
    assert sum_multiples(20, (3, 6)) == 63


def test_accepts_an_empty_divisor_collection() -> None:
    assert sum_multiples(10, ()) == 0


def test_accepts_a_zero_limit() -> None:
    assert sum_multiples(0, (3, 5)) == 0


@pytest.mark.parametrize("limit", [-1, -10])
def test_rejects_negative_limits(limit: int) -> None:
    with pytest.raises(ValueError, match="non-negative"):
        sum_multiples(limit, (3, 5))


def test_rejects_zero_as_a_divisor() -> None:
    with pytest.raises(ValueError, match="zero"):
        sum_multiples(10, (0, 5))
