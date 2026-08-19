# pymath

`pymath` is a Python math-practice lab. Each exercise is a place to work from
examples to a correct program, test the result, improve it, and explain why it
works.

The repository deliberately separates practice solutions from reusable code:

- `exercises/` contains individual problems and your solutions.
- `tests/` contains examples and edge cases for those problems.
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
   uv run pytest tests/exercises/number_theory/test_p001_divisors.py
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

## When reusable code belongs in `src/pymath`

Do not extract a helper after seeing it once. Move an idea into `src/pymath`
when at least two exercises use it, its behavior is clear, and it has dedicated
tests. This keeps the project focused on learning rather than scaffolding.
