# Learning roadmap

## Status key

- `[ ]` not started
- `[~]` in progress
- `[x]` complete and explainable

A problem is complete when its tests pass and you can explain the algorithm,
important edge cases, and approximate time and space complexity.

## Set 1: Foundations

- `[x]` **P000 — Sum of multiples** (worked example)
  - Practice: loops, modulo, validation, and avoiding duplicate counting
- `[x]` **P001 — Positive divisors**
  - Practice: factor pairs, square roots, ordering, and `O(sqrt(n))` thinking
- `[x]` **P002 — Primality test**
  - Practice: definitions, boundary cases, divisibility, and early exits
- `[ ]` **P003 — Greatest common divisor**
  - Practice: Euclid's algorithm, invariants, and zero/negative inputs
- `[ ]` **P004 — Fibonacci sequence**
  - Practice: iterative state, sequence construction, and input validation
- `[x]` **P005 — Prime factorization**
  - Practice: repeated division and combining earlier number-theory ideas

Suggested order: P001, P002, P003, P004, P005.

## Later sets

### Set 2: Algebra and sequences

- Linear equations and small systems
- Arithmetic and geometric sequences
- Polynomial evaluation
- Integer powers and fast exponentiation

### Set 3: Counting and probability

- Permutations and combinations
- Pascal's triangle
- Exact probability with `fractions.Fraction`
- Small Monte Carlo experiments

### Set 4: Linear algebra

- Vector operations
- Matrix multiplication
- Determinants of small matrices
- Gaussian elimination

### Set 5: Numerical methods

- Bisection root finding
- Newton's method
- Numerical derivatives
- Numerical integration

These later sets are intentionally not scaffolded yet. Add them as the first
set reveals the right difficulty and pace.
