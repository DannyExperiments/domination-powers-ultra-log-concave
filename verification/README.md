# Verification

The theorem is proved analytically. The computations here **corroborate** the proof; none of them is load-bearing.

- `src/exact_logconcavity.py`: counts dominating k-sets of P_n^ℓ and C_n^ℓ by bounded compositions, and cross-checks these counts against brute force for n ≤ 14. It then verifies q_k² ≥ q_{k−1}q_{k+1} in exact integer arithmetic for n ≤ 90 and ℓ ≤ 11.
- `src/intermediate_claims.py`: for paths with n ≤ 18 and ℓ ≤ 3, checks the formula for R_k against direct deletion, checks A_k ≥ B_k, and checks that A_k, B_k and R_k never decrease.
- `src/positive_control.py`: shows that the same test detects failures. It finds the star K_{1,4}, whose normalized domination sequence is not log-concave.

Replay everything with `python3 scripts/replay.py`; it compares the output with `logs/`. The independent model audits ran further exact checks: n ≤ 150, ℓ ≤ 30, brute-force validation of the reductions, and 50,000 random trials of the comparison lemma. See `audits/public_safe_reports/MATHEMATICAL_AUDIT.md`.
