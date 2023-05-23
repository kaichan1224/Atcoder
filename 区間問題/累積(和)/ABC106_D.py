import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
2 3 1
1 1
1 2
2 2
1 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
cnt[l][r] :=区間[l,r]の列車の台数
・データを二次元にプロット→プロットの仕方に注意!
・ある長方形区間内に含まれるような個数問題に帰着すると、二次元累積和
で高速化することができる
"""
#--------------------------------------------------------------
N,M,Q = MAP()
cnt = [[0]*(N+2) for _ in range(N+2)]
for m in range(M):
    l,r = MAP()
    cnt[l][r] += 1

for l in range(1,N+1):
    for r in range(1,N+1):
        cnt[l][r+1] += cnt[l][r]

for l in range(1,N+1):
    for r in range(1,N+1):
        cnt[l+1][r] += cnt[l][r]

for _ in range(Q):
    p,q = MAP()
    ans = cnt[q][q] + cnt[p-1][p-1] -cnt[q][p-1] - cnt[p-1][q]
    print(ans)






