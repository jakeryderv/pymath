import pytest

from exercises.p003_gcd import gcd

pytestmark = pytest.mark.skip(reason="P003 has not been started")


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (54, 24, 6),
        (17, 13, 1),
        (8, 12, 4),
        (12, 8, 4),
        (-8, 12, 4),
        (8, -12, 4),
        (-8, -12, 4),
        (17, 0, 17),
        (0, 17, 17),
        (0, 0, 0),
    ],
)
def test_returns_non_negative_gcd(a: int, b: int, expected: int) -> None:
    assert gcd(a, b) == expected
