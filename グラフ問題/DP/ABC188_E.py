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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
考察
*買った回数>=売った回数→これは間違い1kgだけ買い売るとかいてある!
*有向木である(サイクルの心配なし)→DAGはDPを考えることが出来る
*探索部分において,買い値がAmin,売り値がAmaxなら最適
*DP?

ポイント
dp[i]:i番目の街から出発したときの売値の最大値
街iで買った場合の利益の最大値はdp[i]-A[i]
dp[i]=max(dp[i],dp[j],A[j]){j:iから到達可能な街}
"""
######################################################
N,M = MAP()
A = LIST()
G = [[] for _ in range(N)]
for _ in range(M):
    x,y = MAP()
    x,y = x-1,y-1
    G[x].append(y)

#dp[i]:一番安い金の価格
#→それぞれの街において過去一番安いところで金を買った場合の金額が分かるので
#それを元にそれぞれの街で金を売った場合の利益を計算できる
dp = [-INF]*N
ans = -INF
#有向グラフの向きは X→Y
for v in range(0,N):
    for nv in G[v]:
        dp[v] = max(dp[v],dp[nv],A[nv])
    ans = max(ans,dp[v]-A[v])
print(ans)





