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
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
5 3
1 2 2 4 5



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・期待値の線形性を生かせそうな問題
・あらかじめ期待値を求めておいて範囲を決めて累積和で隣接K個の期待値を調べれば良い?

<キーワード>
・期待値+累積和

<ポイント>

"""
#--------------------------------------------------------------
N,K = MAP()
P = LIST()
Psum = []
def sumP(a):
    return a*(a+1)//2
for p in P:
    Psum.append(sumP(p)/p)

ruisekisumP = [0]+list(accumulate(Psum))
ans = 0
for i in range(N-K+1):
    ans = max(ans,(ruisekisumP[i+K]-ruisekisumP[i]))
print(ans)
    
