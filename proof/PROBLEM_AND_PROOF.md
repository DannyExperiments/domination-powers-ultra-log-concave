# Problem and proof

## Problem

Galvin and Zhang, *The domination polynomial of powers of paths and cycles*, Discrete Math. 350(3) (2027) 115520, Conjecture 1.7 (Conjecture 1.8 in arXiv:2408.12731). Let γ_k(H) be the number of dominating sets of size k. In the ℓ-th power G^ℓ, vertices at distance at most ℓ are adjacent. The conjecture: for all n ≥ 0 and ℓ ≥ 1, the sequences γ_k(P_n^ℓ) and γ_k(C_n^ℓ) are ultra log-concave, that is, q_k = γ_k / C(n,k) is log-concave in k. Galvin and Zhang verified it for n, ℓ ≤ 500.

## Proof

1. **Deletion probability.** Delete a uniformly random member from a uniformly random k-set; the result is a uniformly random (k−1)-set. So R_k = q_{k−1}/q_k is the probability that a uniform dominating k-set stays dominating after a uniformly random member is deleted. Log-concavity of q is equivalent to R_k never decreasing.
2. **Compositions.** A dominating set of C_n^ℓ, read from a marked member, is a composition of n with all parts in [1, 2ℓ+1], and these are uniformly distributed. For P_n^ℓ, the interior gaps lie in [1, 2ℓ+1] and the two end gaps in [0, ℓ]. Deleting a member merges its two neighbouring gaps.
3. **Comparison lemma.** Let a be log-concave with no internal zeros, and let b = a * 1_[1,r]. Then a(u)b(v) ≥ b(u)a(v) for u ≤ v. So adding one more bounded part to the remainder makes the merged pair stochastically smaller, given the total. This gives R_k ≤ R_{k+1} for cycles.
4. **Paths.** Write R_k = ((k−2)A_k + 2B_k)/k, where A_k is the probability of a safe interior deletion and B_k that of a safe end deletion. Both are monotone by the lemma. A deficit-swap injection gives A_k ≥ B_k, and the weight on A_k grows with k. So R_k is nondecreasing.

See [`../paper/manuscript.pdf`](../paper/manuscript.pdf).

## Priority

The published paper of Galvin and Zhang reports, in Section 1, that Zheng and Qin proposed an affirmative resolution by a different approach while the paper was under review. It cites this as a personal communication. That work is not public, and this proof was obtained independently of it.
