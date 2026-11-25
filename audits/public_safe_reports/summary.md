# Public-safe audit summaries (2026-11-25)

**Lane 1 (hostile).** No invalid step. Checked:
- the TP2/Toeplitz closure;
- the inequality a(u)b(v) ≥ b(u)a(v);
- the direction of the stochastic order;
- uniformity and exchangeability of the cycle gaps;
- the path decomposition of R_k;
- the ranges in the A_k ≥ B_k swap;
- the final averaging step.

Exact checks: brute force for n ≤ 14, and 3,226 (n, ℓ, k) instances of the intermediate claims. Eight expository requests were incorporated.

**Lane 2 (reconstruction).** The auditor proved the conjecture before reading the note, using the same architecture: deletion ratio, bounded compositions, a PF2 likelihood-ratio comparison, and A_k ≥ B_k via an interval argument. Equality holds only in trivial ranges. No extension beyond powers of paths and cycles is claimed.

**Lane 3 (scope, computation, formalization).** The statement is exact. The auditor's independent exact computations:
- brute force against a direct-domination DP, n ≤ 18: no mismatch;
- log-concavity for n ≤ 150, ℓ ≤ 30: no violation;
- brute-force validation of the cycle and path reductions, n ≤ 15;
- 50,000 random trials of the comparison lemma, including shifted supports and zero weights: no violation; a negative control shows the log-concavity hypothesis is necessary;
- a positive control (the star K_{1,4}) is flagged.

Formalization in Lean/mathlib is estimated to be feasible at 3–6k lines.

## Literature and priority (2026-11-26)
- **Status:** published as Discrete Math. 350(3) (2027) 115520. Its reference list adds a personal communication by J. Zheng and X. Qin titled "Ultra-log-concavity of domination sequences of powers of paths and cycles". The published text could not be read automatically, and no public Zheng–Qin preprint was found. Priority is therefore uncertain.
- **Theorem search:**
  - No identical or stronger published result.
  - The domination polynomials of these graphs are not real-rooted (checked for n ≤ 25), so Newton's inequalities do not apply.
  - Matroid/Lorentzian methods do not apply.
  - Log-concavity of bounded-composition counts (Belbachir–Szalay) is weaker.
- **Architecture:** every ingredient is standard. They are PF2 convolution (Hoggar, Karlin, Stanley), likelihood-ratio order (Shaked–Shanthikumar, Efron) and composition encodings (Arocha–Llano for ℓ = 1). The manuscript cites them.
