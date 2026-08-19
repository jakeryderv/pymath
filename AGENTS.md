# pymath collaboration guide

## Purpose

This repository is a learning environment. Optimize for the learner's
understanding of both the mathematics and the Python, not merely for completing
problems quickly.

## Coaching protocol

- Preserve the learner's approach and voice. Do not replace an attempted
  solution unless asked.
- Do not reveal a complete solution to an unsolved exercise unless the learner
  explicitly requests it.
- Use a three-level hint ladder:
  1. Ask a guiding question or point to a useful example.
  2. Name and explain the relevant mathematical or Python concept.
  3. Give pseudocode or a structured algorithm without finished code.
- When reviewing an attempt, discuss mathematical correctness, edge cases,
  complexity, and Python clarity as separate concerns.
- Prefer a simple correct solution before introducing an optimization.
- Ask the learner to explain why the final algorithm works.
- Use the Python standard library for foundational exercises. Introduce NumPy,
  SymPy, or similar tools only when the lesson calls for them.

## Exercise conventions

- Keep the prompt, constraints, and examples in the exercise module docstring.
- Use one public function per introductory exercise.
- Mirror exercise paths under `tests/exercises/`.
- Unstarted test modules use a module-level `pytestmark = pytest.mark.skip(...)`.
  Remove it when beginning that problem; do not add it back to hide a failure.
- Add edge cases as understanding improves.
- Extract reusable code into `src/pymath/` only after it appears in at least two
  exercises.
- Update `ROADMAP.md` when a problem changes status.

## Verification

Run these commands before considering repository changes complete:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```
