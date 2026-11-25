# Reproducibility
Nothing here is load-bearing; the proof is analytic.
- `python3 -I verification/src/exact_logconcavity.py` → brute-force cross-check n ≤ 14, then `violations: 0` for n ≤ 90, ℓ ≤ 11 (exact integers).
- `python3 -I verification/src/intermediate_claims.py` → `step violations: 0` (paths, n ≤ 18, ℓ ≤ 3).
- `python3 -I verification/src/positive_control.py` → finds a graph (the star K_{1,4}) whose normalized domination sequence is not log-concave, showing that the test detects failures.
- Paper: `cd paper && latexmk -pdf manuscript.tex`.
