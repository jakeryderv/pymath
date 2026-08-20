import pytest

from exercises.p001_divisors import divisors


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, [1]),
        (2, [1, 2]),
        (12, [1, 2, 3, 4, 6, 12]),
        (25, [1, 5, 25]),
        (97, [1, 97]),
    ],
)
def test_returns_sorted_positive_divisors(n: int, expected: list[int]) -> None:
    assert divisors(n) == expected


@pytest.mark.parametrize("n", [0, -1, -12])
def test_rejects_non_positive_inputs(n: int) -> None:
    with pytest.raises(ValueError, match="positive"):
        divisors(n)
