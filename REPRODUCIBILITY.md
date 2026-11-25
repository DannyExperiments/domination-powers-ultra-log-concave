# Reproducibility

Nothing here is load-bearing; the proof is analytic.

| What | Command | Expected |
|---|---|---|
| Integrity and privacy | `python3 -I scripts/verify_repository.py` | `OK: … hashed files, privacy scan clean` |
| Exact computations | `python3 -I scripts/replay.py` | `violations: 0`, `step violations: 0`, positive control `FAILURE FOUND` (K_{1,4}); all outputs match `verification/logs/` |
| Paper | `cd paper && latexmk -pdf manuscript.tex` | 4 pages, no warnings |
| Explorer | unzip `visualization/domination-explorer.zip`, open `index.html` | offline 3D figure |

Each of these also runs in GitHub Actions (badges in `README.md`).
