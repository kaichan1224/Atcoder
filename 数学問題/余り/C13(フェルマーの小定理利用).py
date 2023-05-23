import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
10 0
0 0 0 0 0 1 2 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・片方全探索して、もう片方は一意に定まることを利用するような問題に見えるが、
A[i]*A[j] % mod = P
について、A[j] = P//A[i] % modとしてもうまくいかないことがある
->これをどう対処するかが鍵

A[i]*A[j] % mod = 0

<キーワード>
・余りの計算について

<ポイント>
○余りの計算に関するTIPS
・足し算、掛け算、引き算については、計算の途中で余りを取っても正しく計算することができるため、
値が大きくなる前にmodを取ることで大きな値で計算することを防ぐことができる
・累乗のあまりについては、繰り返し二乗法を用いればよくpythonでは、pow()で可能
・割り算については、フェルマーの小定理を利用することで正しく計算できるようになる
・0で割る可能性があるときは必ず場合分けするように!!!!!!!
"""
#--------------------------------------------------------------
def division_mod(a,b,mod):#a//b%modを正確に求める関数
    return a*pow(b,mod-2,mod)%mod

N,P = MAP()
A = LIST()
for i in range(N):
    A[i] %= mod
for i in range(N):
    A[i] %= mod
d = defaultdict(int)
for a in A:
    d[a%mod] += 1
ans = 0
if P==0:#0での割り算は例外で処理する    
    for i,a in enumerate(A):
        if a==0:
            ans += N-1
        else:
            ans += d[0]
    print(ans//2)
else:
    for i,a in enumerate(A):
        if P//a%mod != a:
            ans += d[division_mod(P,a,mod)]
        else:
            ans += d[division_mod(P,a,mod)] - 1
    print(ans//2)

    
    