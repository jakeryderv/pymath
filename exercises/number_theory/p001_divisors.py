"""P001: find the positive divisors of an integer.

Implement ``divisors`` so it returns every positive divisor of ``n`` in
ascending order.

Examples:
    divisors(1) == [1]
    divisors(12) == [1, 2, 3, 4, 6, 12]
    divisors(25) == [1, 5, 25]

Constraints:
    ``n`` must be positive. Raise ``ValueError`` otherwise.

Stretch goal:
    Find factor pairs without checking every integer from 1 through ``n``.
"""

import math


def divisors(n: int) -> list[int]:
    """Return the positive divisors of ``n`` in ascending order."""
    if n <= 0:
        raise ValueError("n must be positive")

    div_set = set()
    stop = math.isqrt(n)

    for d in range(1, stop + 1):
        q, r = divmod(n, d)

        if r == 0:
            div_set.update([d, q])

    return sorted(div_set)
