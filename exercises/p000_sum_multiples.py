"""Worked example: sum multiples below a limit.

Return the sum of every non-negative integer below ``limit`` that is divisible
by at least one value in ``divisors``. Count a number only once when more than
one divisor matches it.

Examples:
    sum_multiples(10, (3, 5)) == 23
    sum_multiples(6, (2,)) == 6

This completed example demonstrates the expected shape of an exercise. Its
tests cover normal behavior, boundaries, overlapping matches, and invalid
input.
"""

from pymath.exercise_catalog import ExerciseMetadata

METADATA = ExerciseMetadata(
    problem_id="P000",
    title="Sum of multiples",
    categories=("arithmetic", "number-theory"),
    concepts=("loops", "modulo", "validation", "deduplication"),
)


def sum_multiples(limit: int, divisors: tuple[int, ...]) -> int:
    """Return the sum of numbers below ``limit`` matching any divisor."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    if any(divisor == 0 for divisor in divisors):
        raise ValueError("divisors cannot contain zero")

    return sum(
        number
        for number in range(limit)
        if any(number % divisor == 0 for divisor in divisors)
    )
