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
15
1 2 1 1 1 6 2 6 9 10 6 12 13 12
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・探索は制約的に1回しかできない→dfsしながらDP
・帰りがけのDP

<キーワード>


<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
G = [[] for _ in range(N)]
for i in range(1,N):
    G[i].append(A[i-1]-1)
    G[A[i-1]-1].append(i)

dp = [0]*N

def dfs(v,pre):
    global dp
    #頂点が初めて探索されるタイミング(行きがけ)
    for u in G[v]:
        if u!=pre:
            dfs(u,v)
            #子の一つが探索終わったタイミング
    #頂点が探索終えたタイミング(帰りがけ)
    if pre!=-1:
        dp[pre] += dp[v]+1
dfs(0,-1)
print(*dp)
    
     
