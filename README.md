# pymath

`pymath` is a Python math-practice lab. Each exercise is a place to work from
examples to a correct program, test the result, improve it, and explain why it
works.

The repository deliberately separates practice solutions from reusable code:

- `exercises/` is a flat, numbered catalog of individual problems and your
  solutions.
- `tests/exercises/` mirrors that flat catalog with examples and edge cases.
- `src/pymath/` is for techniques worth reusing across several problems.
- `notes/` records useful ideas and recurring mistakes.
- `notebooks/` is a scratch space for experiments and visualizations.
- `ROADMAP.md` tracks the learning path and problem status.

## Quick start

This project uses Python 3.12 and
[uv](https://docs.astral.sh/uv/) for its environment.

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

The default test suite stays green. Unstarted exercises have tests that are
skipped until you activate them.

## Work on an exercise

1. Choose the next problem from `ROADMAP.md`.
2. Read its docstring and work through the examples by hand.
3. Open the matching test file and remove its module-level `pytestmark` line.
4. Run only that problem's tests. For example:

   ```bash
   uv run pytest tests/exercises/test_p001_divisors.py
   ```

5. Implement the simplest correct solution.
6. Add at least one edge case of your own.
7. Improve the solution if there is a clear reason to do so.
8. Update `ROADMAP.md` and capture the main lesson in `notes/`.

It is normal for the targeted test to fail immediately after activation. That
is the red step in the red-green-refactor cycle.

## Asking Codex for help

By default, Codex should coach rather than reveal the answer. Ask for:

- **Hint 1** for a question that points you in the right direction.
- **Hint 2** for the relevant mathematical idea.
- **Hint 3** for pseudocode or a structured approach.
- **Full solution** only when you intentionally want to study one.
- **Review** when you have an attempt and want feedback without replacement.

The complete collaboration rules live in `AGENTS.md`.

## Exercise metadata and discovery

Every exercise module defines `METADATA` with its problem ID, title,
categories, and concepts. Categories and concepts are collections, so an
exercise can belong to more than one mathematical area without being forced
into a single directory.

Use the catalog API to inspect or group the complete problem set:

```python
from pymath.exercise_catalog import discover_exercises

number_theory = [
    exercise
    for exercise in discover_exercises()
    if "number-theory" in exercise.categories
]
```

The metadata describes an exercise. Learning progress remains in
`ROADMAP.md`.

## When reusable code belongs in `src/pymath`

Do not extract a helper after seeing it once. Move an idea into `src/pymath`
when at least two exercises use it, its behavior is clear, and it has dedicated
tests. This keeps the project focused on learning rather than scaffolding.
