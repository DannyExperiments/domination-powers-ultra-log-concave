# Ultra log-concavity of the domination polynomials of powers of paths and cycles

**Answer: yes.** For all n ≥ 0 and ℓ ≥ 1, the sequences γ_k(P_n^ℓ)/C(n,k) and γ_k(C_n^ℓ)/C(n,k) are log-concave. This repository gives an independent, self-contained proof of Conjecture 1.8 of Galvin and Zhang (Conjecture 1.7 in the published version). The published paper reports that Zheng and Qin proposed an affirmative resolution by a different approach (personal communication; not yet public).

## The problem
D. Galvin and Y. Zhang, *The domination polynomial of powers of paths and cycles*, Discrete Math. **350**(3) (2027) 115520, [doi:10.1016/j.disc.2026.115520](https://doi.org/10.1016/j.disc.2026.115520) ([arXiv:2408.12731](https://arxiv.org/abs/2408.12731)), Conjecture 1.8. Here γ_k(H) counts dominating sets of size k, and G^ℓ joins vertices at distance at most ℓ. Galvin and Zhang verified the conjecture for n, ℓ ≤ 500.

## The result and the idea
The ratio q_{k−1}/q_k is the probability that a uniformly random dominating k-set stays dominating after a uniformly random member is deleted. So log-concavity amounts to this probability being nondecreasing in k. Dominating sets are compositions of n (or n−1) with parts in [1, 2ℓ+1] (end parts in [0, ℓ] for paths). Deleting a member merges two adjacent parts. Adding one more bounded part to the remainder makes the merged sum stochastically smaller, by a likelihood-ratio argument for log-concave sequences. For paths, a deficit-swap injection compares deleting an end member with deleting an interior one.

- Paper: [`paper/manuscript.pdf`](paper/manuscript.pdf) · source [`paper/manuscript.tex`](paper/manuscript.tex)
- Reproduce: [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)

[![verify](https://github.com/DannyExperiments/domination-powers-ultra-log-concave/actions/workflows/verify.yml/badge.svg)](https://github.com/DannyExperiments/domination-powers-ultra-log-concave/actions/workflows/verify.yml) [![pdf](https://github.com/DannyExperiments/domination-powers-ultra-log-concave/actions/workflows/pdf.yml/badge.svg)](https://github.com/DannyExperiments/domination-powers-ultra-log-concave/actions/workflows/pdf.yml)

## Verification status
| Item | Status |
|---|---|
| Proof | Complete, analytic; does not rely on computation |
| Independent AI audits | Three independent model audits, all PASS; not peer review |
| Computation | Corroborating only: exact check n ≤ 90, ℓ ≤ 11; intermediate claims; positive control |
| Lean | Not attempted |
| Peer review | Not refereed |
| Priority | **Not first**: Zheng–Qin proposed a resolution earlier (reported in Galvin–Zhang, Discrete Math. 2027, §1); this is an independent proof — see [`STATUS.md`](STATUS.md) |

## Citation
See [`CITATION.cff`](CITATION.cff) (added after authorship approval).
