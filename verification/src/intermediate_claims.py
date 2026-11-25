"""Exact check of the intermediate claims for paths (corroborating): the R_k formula against
direct deletion, A_k >= B_k, and monotonicity of A_k, B_k, R_k, for n<=18, l<=3."""
# exact check of the proof's intermediate claims for paths: A_k, B_k monotone, A_k>=B_k, R_k formula
from fractions import Fraction as F
from math import comb
import itertools
def comps(n,l,k):
    r=2*l+1
    def rec(rem,parts,out):
        pass
    res=[]
    # vectors (E_L, g_1..g_{k-1}, E_R)
    def gen(prefix,left,slots):
        if slots==0:
            if 0<=left<=l: res.append(prefix+(left,))
            return
        lo,hi=(0,l) if not prefix else (1,r)
        for v in range(lo,min(hi,left)+1): gen(prefix+(v,),left-v,slots-1)
    gen((),n-1,k)
    return res
bad=0
for l in range(1,4):
    r=2*l+1
    for n in range(2,19):
        prevA=prevB=prevR=None
        for k in range(2,n+1):
            V=comps(n,l,k)
            if not V: prevA=prevB=prevR=None; continue
            N=len(V)
            B=F(sum(1 for v in V if v[0]+v[1]<=l),N)
            A=F(sum(1 for v in V if v[1]+v[2]<=r),N) if k>=3 else None
            R=B if k==2 else ((k-2)*A+2*B)/k
            # direct R: delete uniform chosen vertex
            pos=[]
            for v in V:
                s=[v[0]]
                for g in v[1:-1]: s.append(s[-1]+g)
                pos.append(s)
            ok=0
            for s in pos:
                for idx in range(k):
                    t=s[:idx]+s[idx+1:]
                    if t and t[0]<=l and n-1-t[-1]<=l and all(t[i+1]-t[i]<=r for i in range(len(t)-1)): ok+=1
            Rd=F(ok,N*k)
            if Rd!=R: bad+=1; print("R mismatch",n,l,k)
            if A is not None and A<B: bad+=1; print("A<B",n,l,k)
            if prevB is not None and B<prevB: bad+=1;print("B dec",n,l,k)
            if prevA is not None and A is not None and A<prevA: bad+=1;print("A dec",n,l,k)
            if prevR is not None and R<prevR: bad+=1;print("R dec",n,l,k)
            prevA,prevB,prevR=A,B,R
print("step violations:",bad)
