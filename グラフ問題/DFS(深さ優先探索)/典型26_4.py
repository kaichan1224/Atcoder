import io
import sys
sys.setrecursionlimit(10**7)
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
6
1 3
2 4
3 5
2 5
3 6

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""


"""
#--------------------------------------------------------------
N = INT()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    G[a-1].append(b-1)
    G[b-1].append(a-1)
#0:white,1:black
dist = [-1]*N
#dist[0] = 0
def dfs(v,pre,coler):
    dist[v] = coler
    for nxt in G[v]:
        if nxt!=pre:
            dfs(nxt,v,1-coler)
dfs(0,-1,0)
white = []
black = []
for i in range(N):
    if dist[i]==0:
        white.append(i+1)
    else:
        black.append(i+1)
if len(white)>len(black):
    print(*white[:N//2])
else:
    print(*black[:N//2])







