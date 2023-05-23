import io
import sys
sys.setrecursionlimit(10**7)
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
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
6 5
2 3
3 4
3 5
5 6
2 6
7
1 1
2 2
2 0
2 3
4 1
6 0
4 3

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""


"""
#--------------------------------------------------------------
ans = 0
N,M = MAP()
G = [[] for i in range(N)]
a = []
def dfs(v,pre,depth,k):
    global a
    if depth==k+1:
        return 
    a.append(v+1)
    for u in G[v]:
        if u!=pre:
            dfs(u,v,depth+1,k)
for i in range(M):
    a,b = MAP()
    G[a-1].append(b-1)
    G[b-1].append(a-1)
Q = INT()
for i in range(Q):
    a = []
    x,k = MAP()
    x -= 1
    dfs(x,-1,0,k)
    print(sum(set(a)))






