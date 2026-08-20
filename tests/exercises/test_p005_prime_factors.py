import pytest

from exercises.p005_prime_factors import prime_factors


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (2, [2]),
        (12, [2, 2, 3]),
        (25, [5, 5]),
        (84, [2, 2, 3, 7]),
        (97, [97]),
    ],
)
def test_returns_prime_factors_in_ascending_order(n: int, expected: list[int]) -> None:
    assert prime_factors(n) == expected


@pytest.mark.parametrize("n", [-10, 0, 1])
def test_rejects_values_below_two(n: int) -> None:
    with pytest.raises(ValueError, match="at least 2"):
        prime_factors(n)
