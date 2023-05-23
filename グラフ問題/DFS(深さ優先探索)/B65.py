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
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
"""
<考察>
・木をDPしたい場合は,dfs

<キーワード>

<ポイント>
・社員の直属の部下の階級がそれぞれr1,r2,r3,..である時、社員xの階級は次式で
(社員xの階級)=max(r1,r2,r3,..)+1
"""
#--------------------------------------------------------------
N,T = MAP()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

dp = [0]*N
def dfs(v,pre,depth):
    print(v,depth)
    global dp
    #頂点が初めて探索されるタイミング(行きがけ)
    for u in G[v]:
        if u!=pre:
            dfs(u,v,depth+1)
            #子の一つが探索終わったタイミング
    #頂点が探索終えたタイミング(帰りがけ)
    if pre!=-1:
        dp[pre] = max(dp[pre],dp[v]+1)#depth
dfs(T-1,-1,0)
print(*dp)