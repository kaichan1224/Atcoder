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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
8 12 1 5
0 1
0 2
0 4
1 7
1 3
2 4
3 2
3 6
5 3
5 4
6 5
6 7
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・s-tパスを実際に出力する問題

<Why>
・prev[nxt] = nowだと通って、prev[now] = nxtはダメだったのはなぜ?
・for nxt in G[now]:
    if dist[nxt]==-1:
        prev[nxt] = now
        (略)
"""
#--------------------------------------------------------------
N,M,s,t = MAP()
G = [[] for _ in range(N)]
dist = [False]*N
par = [-1]*N
dist[s] = True
for _ in range(M):
    a,b = MAP()
    G[a].append(b)
que = deque([s])
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]:
            continue
        que.append(nxt)
        par[nxt] = now
        dist[nxt] = True
ans = []
now = t
while now != -1:
    ans.append(now)
    now = par[now]
ans.reverse()
print(len(ans))
print(*ans)
    