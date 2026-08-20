"""Discover exercises and expose their descriptive metadata."""

import re
from dataclasses import dataclass
from importlib import import_module
from pkgutil import iter_modules

_EXERCISE_MODULE = re.compile(r"p\d{3}_[a-z0-9_]+")


@dataclass(frozen=True, slots=True)
class ExerciseMetadata:
    """Descriptive information stored alongside an exercise."""

    problem_id: str
    title: str
    categories: tuple[str, ...]
    concepts: tuple[str, ...]

    def __post_init__(self) -> None:
        """Reject metadata that would make catalog filtering ambiguous."""
        if not re.fullmatch(r"P\d{3}", self.problem_id):
            raise ValueError("problem_id must use the form P000")
        if not self.title:
            raise ValueError("title must not be empty")
        if not self.categories:
            raise ValueError("categories must not be empty")
        if len(set(self.categories)) != len(self.categories):
            raise ValueError("categories must not contain duplicates")
        if len(set(self.concepts)) != len(self.concepts):
            raise ValueError("concepts must not contain duplicates")


def discover_exercises() -> tuple[ExerciseMetadata, ...]:
    """Return metadata for every flat exercise module, ordered by problem ID."""
    package = import_module("exercises")
    discovered: list[ExerciseMetadata] = []

    for module_info in iter_modules(package.__path__):
        if not _EXERCISE_MODULE.fullmatch(module_info.name):
            continue

        module = import_module(f"exercises.{module_info.name}")
        metadata = getattr(module, "METADATA", None)
        if not isinstance(metadata, ExerciseMetadata):
            raise TypeError(
                f"{module.__name__} must define ExerciseMetadata as METADATA"
            )

        expected_id = module_info.name[:4].upper()
        if metadata.problem_id != expected_id:
            raise ValueError(
                f"{module.__name__} has problem_id {metadata.problem_id!r}; "
                f"expected {expected_id!r}"
            )

        discovered.append(metadata)

    problem_ids = [metadata.problem_id for metadata in discovered]
    if len(set(problem_ids)) != len(problem_ids):
        raise ValueError("exercise problem IDs must be unique")

    return tuple(sorted(discovered, key=lambda metadata: metadata.problem_id))
