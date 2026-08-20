import pytest

from exercises.p002_is_prime import is_prime


@pytest.mark.parametrize("n", [-10, -1, 0, 1])
def test_values_below_two_are_not_prime(n: int) -> None:
    assert is_prime(n) is False


@pytest.mark.parametrize("n", [2, 3, 5, 29, 97])
def test_recognizes_primes(n: int) -> None:
    assert is_prime(n) is True


@pytest.mark.parametrize("n", [4, 9, 21, 49, 100])
def test_recognizes_composites(n: int) -> None:
    assert is_prime(n) is False
