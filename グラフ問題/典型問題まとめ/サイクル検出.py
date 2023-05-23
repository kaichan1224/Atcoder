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
5 5
0 2
4 1
1 2
2 4
4 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""

"""
#--------------------------------------------------------------
N,M = MAP()
G = [[] for _ in range(N)]
#deg[v]:vを始点とする辺の本数(出次数)
deg = [0]*N
for _ in range(M):
    a,b = MAP()
    G[b].append(a)
    deg[a] += 1

que = deque()
for i in range(N):
    G[i].sort() #問題文の指示次第ではある
    if deg[i]==0:
        que.append(i)
        
order = []
while que:
    now = que.popleft()
    order.append(now)
    for nxt in G[now]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            que.append(nxt)

order.reverse()
#print(*order)
if len(order)==N:
    print("No")
else:
    print("Yes")
