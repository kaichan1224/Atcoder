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
_INPUT = """\
8 7
1 2
2 3
2 4
5 6
6 7
6 8
7 8

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・制約的にN,Mが小さいので、dfsで全然間に合いそう!

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M = MAP()
G = [[] for _ in range(N)]
for _ in range(M):
    u,v = MAP()
    u,v = u-1,v-1
    G[u].append(v)
    G[v].append(u)
ans = 0
dist = [False]*N
for v in range(N):
    if dist[v]==False:
        stack = [(v,-1)]
        dist[v] = True
        flag = False#閉路なし
        while stack:
            now,pre = stack.pop()
            for nxt in G[now]:
                if nxt!=pre:
                    if dist[nxt]==True:
                        flag = True
                    else:
                        dist[nxt] = True
                        stack.append((nxt,now))
        if not flag:
            ans += 1
print(ans)
        
