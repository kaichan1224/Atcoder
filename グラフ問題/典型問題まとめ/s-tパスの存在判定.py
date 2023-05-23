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
8 12 5 1
3 6
5 4
0 2
1 7
2 4
0 4
1 3
0 1
6 5
6 7
3 2
5 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""

"""
#--------------------------------------------------------------
N,M,s,t = MAP()
G = [[]*N for _ in range(N)]
dist = [False]*N
dist[s] = True
for _ in range(M):
    a,b = MAP()
    G[a].append(b)
que = deque([s])
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]==False:
            que.append(nxt)
            dist[nxt] = True
if dist[t]:
    print("Yes")
else:
    print("No")
    