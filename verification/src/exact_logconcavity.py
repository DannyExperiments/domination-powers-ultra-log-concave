"""Exact check of Theorem 1.2 (corroborating, not load-bearing): counts gamma_k for P_n^l, C_n^l
by bounded compositions, cross-checked against brute force for n<=14, then verifies
q_k^2 >= q_{k-1} q_{k+1} in exact integer arithmetic for n<=90, l<=11."""
from math import comb
from fractions import Fraction as F
def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): c[i+j]+=x*y
    return c
def ind(lo,hi): return [0]*lo+[1]*(hi-lo+1)
def path_counts(n,l):
    r=2*l+1; g=[0]*(n+1)
    # k chosen: E_L,E_R in [0,l], k-1 gaps in [1,r], total n-1
    base=conv(ind(0,l),ind(0,l)); cur=base
    for k in range(1,n+1):
        g[k]=cur[n-1] if n-1<len(cur) else 0
        cur=conv(cur,ind(1,r))
    return g
def cycle_counts(n,l):
    r=2*l+1; g=[0]*(n+1); cur=ind(1,r)
    for k in range(1,n+1):
        c=cur[n] if n<len(cur) else 0
        assert (n*c)%k==0; g[k]=n*c//k
        cur=conv(cur,ind(1,r))
    return g
# brute-force cross-check for small n
import itertools
def brute(n,l,cyc):
    def d(i,j): 
        t=abs(i-j); return min(t,n-t) if cyc else t
    g=[0]*(n+1)
    for m in range(1<<n):
        S=[i for i in range(n) if m>>i&1]
        if all(any(d(i,j)<=l for j in S) for i in range(n)): g[len(S)]+=1
    return g
for n in range(1,15):
    for l in range(1,5):
        assert brute(n,l,False)==path_counts(n,l),(n,l)
        if n>=3: assert brute(n,l,True)==cycle_counts(n,l),(n,l)
print("formulas match brute force n<=14")
bad=0
for n in range(1,91):
    for l in range(1,12):
        for f in (path_counts,cycle_counts):
            if f is cycle_counts and n<3: continue
            g=f(n,l); q=None
            for k in range(1,n+1):
                gk1=g[k+1] if k<n else 0
                if g[k]*g[k]*comb(n,k-1)*(comb(n,k+1) if k<n else 1) < g[k-1]*gk1*comb(n,k)**2: bad+=1; print("VIOLATION",f.__name__,n,l,k)
print("violations:",bad)
