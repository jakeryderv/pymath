import pytest

from pymath.exercise_catalog import ExerciseMetadata, discover_exercises


def test_discovers_every_exercise_in_problem_order() -> None:
    exercises = discover_exercises()

    assert [exercise.problem_id for exercise in exercises] == [
        "P000",
        "P001",
        "P002",
        "P003",
        "P004",
        "P005",
    ]


def test_metadata_supports_multiple_categories() -> None:
    exercises = {exercise.problem_id: exercise for exercise in discover_exercises()}

    assert exercises["P005"].categories == ("number-theory", "arithmetic")


@pytest.mark.parametrize(
    ("problem_id", "message"),
    [("5", "form P000"), ("P005", "categories must not be empty")],
)
def test_metadata_rejects_invalid_required_fields(
    problem_id: str, message: str
) -> None:
    categories = ("number-theory",) if problem_id == "5" else ()

    with pytest.raises(ValueError, match=message):
        ExerciseMetadata(
            problem_id=problem_id,
            title="Prime factorization",
            categories=categories,
            concepts=(),
        )
