"""P003: calculate the greatest common divisor.

Implement Euclid's algorithm and return a non-negative greatest common divisor.
The function should accept negative inputs and define ``gcd(0, 0)`` as 0.

Examples:
    gcd(54, 24) == 6
    gcd(-8, 12) == 4
    gcd(17, 0) == 17
    gcd(0, 0) == 0

Do not call ``math.gcd`` in the exercise solution. You may use it in an
additional test to check your implementation over many inputs.
"""

from pymath.exercise_catalog import ExerciseMetadata

METADATA = ExerciseMetadata(
    problem_id="P003",
    title="Greatest common divisor",
    categories=("number-theory",),
    concepts=("euclidean-algorithm", "invariants", "integers"),
)


def gcd(a: int, b: int) -> int:
    """Return the non-negative greatest common divisor of ``a`` and ``b``."""
    raise NotImplementedError("Solve P003")
