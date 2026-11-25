# Verification (corroborating only)
- `src/exact_logconcavity.py`: composition counts cross-checked against brute force for n ≤ 14, then exact log-concavity for n ≤ 90, ℓ ≤ 11.
- `src/intermediate_claims.py`: for paths with n ≤ 18, ℓ ≤ 3, checks the R_k formula against direct deletion, A_k ≥ B_k, and that A_k, B_k and R_k are monotone.
- `src/positive_control.py`: the same test flags the star K_{1,4}.
