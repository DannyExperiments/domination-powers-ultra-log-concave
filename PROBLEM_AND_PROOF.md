# Problem and proof in brief
**Problem** (Galvin–Zhang, Conjecture 1.8). Is γ_k(G^ℓ)/C(n,k) log-concave in k for G = P_n and G = C_n?

**Proof sketch.**
1. q_{k−1}/q_k = R_k, the chance that a uniform dominating k-set stays dominating after deleting a uniform member. So the conjecture says R_k is nondecreasing.
2. Dominating sets are bounded compositions:
   - cycles: gaps in [1, 2ℓ+1];
   - paths: interior gaps in [1, 2ℓ+1], end gaps in [0, ℓ].
3. Deleting a member merges two adjacent parts. Adding one more bounded part to the remainder makes the merged sum stochastically smaller, by a likelihood-ratio argument for log-concave sequences. So R_k increases for cycles.
4. For paths, R_k averages an end-deletion probability B_k and an interior one A_k, each of which is monotone. A_k ≥ B_k by a swap injection, and the weight on A_k grows with k.

Full details: `paper/manuscript.pdf`.
