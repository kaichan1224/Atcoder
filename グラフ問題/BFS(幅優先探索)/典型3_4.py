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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3
1 2
2 3

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
木の直径を求める問題
頂点0から最も距離の長い頂点を求める→求めた点から最も距離の長い点
が木の直径になる

注:2回目のBFSではindexではなく最大値を出力するように。
"""
######################################################
N = INT()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

que = deque([0])
dist = [-1]*N
dist[0] = 0
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]==-1:
            que.append(nxt)
            dist[nxt] = dist[now] + 1
tmp = dist.index(max(dist))

que = deque([tmp])
dist = [-1]*N
dist[tmp] = 0
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]==-1:
            que.append(nxt)
            dist[nxt] = dist[now] + 1
ans = max(dist)
print(ans+1)






