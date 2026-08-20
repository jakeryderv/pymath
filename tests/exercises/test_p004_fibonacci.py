import pytest

from exercises.p004_fibonacci import fibonacci

pytestmark = pytest.mark.skip(reason="P004 has not been started")


@pytest.mark.parametrize(
    ("count", "expected"),
    [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (7, [0, 1, 1, 2, 3, 5, 8]),
    ],
)
def test_returns_requested_number_of_terms(count: int, expected: list[int]) -> None:
    assert fibonacci(count) == expected


def test_returns_a_new_list_each_time() -> None:
    assert fibonacci(5) is not fibonacci(5)


def test_rejects_negative_counts() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)
