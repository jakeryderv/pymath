"""P005: find the prime factorization of an integer.

Return the prime factors of ``n`` in ascending order. Repeated factors must be
included.

Examples:
    prime_factors(2) == [2]
    prime_factors(12) == [2, 2, 3]
    prime_factors(84) == [2, 2, 3, 7]
    prime_factors(97) == [97]

Constraints:
    ``n`` must be at least 2. Raise ``ValueError`` otherwise.
"""

import math

from pymath.exercise_catalog import ExerciseMetadata

METADATA = ExerciseMetadata(
    problem_id="P005",
    title="Prime factorization",
    categories=("number-theory", "arithmetic"),
    concepts=("primes", "divisibility", "factorization"),
)


def prime_factors(n: int) -> list[int]:
    """
    Return the prime factors of ``n`` in ascending order.

    approach: Sieve of Eratosthenes
    """
    if n < 2:
        raise ValueError("n must be at least 2.")

    stop = math.isqrt(n)
    nums = sorted(range(2, stop + 1))

    i = 0
    while i < len(nums):
        num = nums[i]
        nums = nums[: i + 1] + [x for x in nums[i + 1 :] if x % num != 0]
        i += 1

    factors = []

    for prime in nums:
        while n % prime == 0:
            factors.append(prime)
            n //= prime

    if n > 1:
        factors.append(n)

    return factors
