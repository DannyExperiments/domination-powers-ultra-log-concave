"""Positive control: the same log-concavity test applied to all graphs on <=7 vertices
(edge subsets of K_n, sampled) must find graphs whose normalized domination sequence is
NOT log-concave, showing that the test can detect failures."""
import itertools, random
from math import comb
def dom_counts(n, adj):
    g=[0]*(n+1)
    for m in range(1<<n):
        cov=0
        for i in range(n):
            if m>>i&1: cov|=adj[i]
        if cov==(1<<n)-1: g[bin(m).count('1')]+=1
    return g
def ulc_fails(n,g):
    return [k for k in range(1,n) if g[k]*g[k]*comb(n,k-1)*comb(n,k+1) < g[k-1]*g[k+1]*comb(n,k)**2]
rng=random.Random(0); found=None
for n in range(4,8):
    pairs=list(itertools.combinations(range(n),2))
    for _ in range(3000):
        E=[p for p in pairs if rng.random()<0.35]
        adj=[1<<i for i in range(n)]
        for a,b in E: adj[a]|=1<<b; adj[b]|=1<<a
        g=dom_counts(n,adj); f=ulc_fails(n,g)
        if f: found=(n,E,g,f); break
    if found: break
print("positive control:", "FAILURE FOUND" if found else "none found", found)
