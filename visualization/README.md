# Domination explorer

An interactive 3D figure for the proof. Download [`domination-explorer.zip`](domination-explorer.zip), unzip it, and open `index.html` in a browser. It runs offline with no external libraries.

- **Choose the graph.** Pick a cycle or a path, n up to 60 and ℓ up to 6. It is drawn as a ring you can rotate; click vertices to add or remove them. Covered stretches are shaded and uncovered vertices turn red.
- **Random dominating k-set, then delete a random member.** Watch whether the set survives. For small k deletions usually fail; for large k they rarely do.
- **The chart** shows R(k) = q_{k−1}/q_k for the chosen graph, computed exactly with big-integer composition counts. It never decreases. The panel also confirms q_k² ≥ q_{k−1}q_{k+1} for every k in exact arithmetic.

The GIF shows C₂₄ with ℓ = 1: a random member is deleted from dominating sets of sizes 8–18, next to the exact curve R(k).
