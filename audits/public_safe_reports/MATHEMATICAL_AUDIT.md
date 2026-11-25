# Mathematical audit (25 November 2026)

Three independent Claude instances audited the frozen proof note. Each saw only the frozen note and the original problem, not the other audits or the director's conclusions, and worked without internet access.

| Lane | Verdict | Confidence | Main checks |
|---|---|---|---|
| 1. Hostile line-by-line | PASS, no invalid step | 0.95 | Every step was attacked: TP2 closure, the ratio inequality, the direction of the stochastic order with shifted supports and zero weights, uniformity and exchangeability of the cycle gaps, the R_k decomposition for paths, the ranges in the A_k ≥ B_k swap, and the averaging step. Exact checks: brute force n ≤ 14; 3,226 (n, ℓ, k) instances of the intermediate claims |
| 2. Independent reconstruction | CORRECT | 0.95 | Proved the conjecture before reading the note, with the same architecture. Equality occurs only in trivial ranges. Brute force n ≤ 14; composition formulas n ≤ 69 |
| 3. Scope, computation, formalization | PASS, statement exact | 0.90 | Own exact code: brute force against a direct DP (n ≤ 18); log-concavity for n ≤ 150, ℓ ≤ 30; brute-force validation of the cycle and path reductions (n ≤ 15); 50,000 random trials of the comparison lemma, plus a negative control showing the log-concavity hypothesis is necessary; positive control K_{1,4} |

Editorial repairs adopted in the paper:
- Lemmas 2.1–2.3 are stated precisely, with explicit index ranges, and the comparison is phrased as the likelihood-ratio order implying the stochastic order.
- The reduction to pairs with q_k, q_{k+1} > 0 is made explicit.
- The cycle wrap-around and the small-n conventions are stated.
- The triple used in the swap is named, together with its ranges.
- The final averaging step is written out.

These are AI audits, not peer review.
