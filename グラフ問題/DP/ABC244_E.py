import io
import sys
import math
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
mod = 998244353
######################################################
_INPUT = """\
4 4 4 1 3 2
1 2
2 3
3 4
1 4
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
S→TへK回の移動する際にXが偶数階出現するときの行き方の回数
DPで解く
必要な情報：
現在の移動回数、現在いる頂点、今までXを通った回数が偶数回か奇数回か

<ポイント>
"""
######################################################
N,M,K,S,T,X = MAP()
G = [[] for _ in range(N+1)]
for _ in range(M):
    u,v= MAP()
    G[u].append(v)
    G[v].append(u)
#dp[k][n]:k回目の移動、n頂点についての情報(移動回数)
dp1 = [[0]*(N+1) for _ in range(K+1)]#偶数回のとき
dp2 = [[0]*(N+1) for _ in range(K+1)]#奇数回のとき

#初期値に注意
dp1[0][S] = 1
for i in range(K):
    for u in range(1,N+1):#それぞれの頂点について
        for v in G[u]:#つながっている頂点
            if v==X:#xを通ったら
                dp1[i+1][v] += dp2[i][u]
                dp2[i+1][v] += dp1[i][u]
            else:
                dp1[i+1][v] += dp1[i][u]
                dp2[i+1][v] += dp2[i][u]
            dp1[i+1][v] %= mod
            dp2[i+1][v] %= mod
print(dp1[K][T])
            
            












