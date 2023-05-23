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
"""
<考察>
N=10^5
全ての辺の長さ(重み)が1の木
全ての頂点間の重みの総和を求めたい
主客転倒
重みベースではなく、その区間を何回通るかで考える
→dfsを行い、辺を通った回数を足していく(ちょっと違う)

<ポイント>
ある辺は何個の頂点対における最短経路に含まれるか
→ある辺の答えへの貢献度を考える
点集合(A)→ある辺→点集合(B=N-A)という風に考えると、
辺の貢献度は|A|*|N-A|
→頂点xの部下みたいな感じの頂点の個数はどのようにもとめるか
dp[now] += dp[nxt]で求めることができる
"""
#--------------------------------------------------------------
N = INT()
dp = [0]*N
G = [[] for _ in range(N)]
ab = []
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
    ab.append((a,b))
def dfs(v,pre):
    #print(v)
    dp[v] = 1
    for nxt in G[v]:
        if nxt != pre:
            dfs(nxt,v)
            dp[v] += dp[nxt]
dfs(0,-1)
ans = 0
for i in range(N):
    ans += dp[i]*(N-dp[i])
print(ans)





