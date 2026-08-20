"""P004: generate Fibonacci numbers.

Return the first ``count`` Fibonacci numbers, beginning with 0 and 1.

Examples:
    fibonacci(0) == []
    fibonacci(1) == [0]
    fibonacci(2) == [0, 1]
    fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

Constraints:
    ``count`` must be non-negative. Raise ``ValueError`` otherwise.

Use an iterative solution for this exercise.
"""

from pymath.exercise_catalog import ExerciseMetadata

METADATA = ExerciseMetadata(
    problem_id="P004",
    title="Fibonacci sequence",
    categories=("sequences", "number-theory"),
    concepts=("iteration", "state", "validation"),
)


def fibonacci(count: int) -> list[int]:
    """Return the first ``count`` Fibonacci numbers."""
    raise NotImplementedError("Solve P004")
