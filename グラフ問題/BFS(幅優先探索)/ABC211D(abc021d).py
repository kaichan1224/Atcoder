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
mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
7 8
1 3
1 4
2 3
2 4
2 5
2 6
5 7
6 7

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
最短経路への移動回数
移動できる都市が未到達の場合 cnt[nxt] = cnt[now]
移動できる都市が到達済みの場合 最短経路の値が同じであれば
(dist[nxt]==dist[now]+1),cnt[nxt] += cnt[now]
(遷移前の数を足し合わせることで最短経路の数を更新)
"""
######################################################
N,M = MAP()
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
q = deque([0])
dist = [-1]*N
dist[0] = 0
dp = [0]*N
dp[0] = 1
while q:
    now = q.popleft()
    for nxt in G[now]:
        if dist[nxt]==-1:
            dist[nxt] = dist[now]+1
            q.append(nxt)
            dp[nxt] = dp[now]
            dp[nxt] %= mod
        else:
            if dist[nxt]==dist[now]+1:
                dp[nxt] += dp[now]    
print(dp[N-1]%mod)




