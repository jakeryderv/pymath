"""P002: determine whether an integer is prime.

A prime number is an integer greater than 1 with exactly two positive divisors:
1 and itself.

Examples:
    is_prime(-7) is False
    is_prime(1) is False
    is_prime(2) is True
    is_prime(21) is False
    is_prime(29) is True

Stretch goal:
    Once a straightforward version works, determine the largest possible
    divisor that actually needs to be checked.
"""

import math


def is_prime(n: int) -> bool:
    """Return whether ``n`` is prime."""
    if n < 2:
        return False

    stop = math.isqrt(n)

    for num in range(2, stop + 1):
        if n % num == 0:
            return False

    return True
