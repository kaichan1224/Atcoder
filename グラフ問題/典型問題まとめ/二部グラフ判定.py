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
def YesNo(f): return print("Yes" if f else "No")
INF = float('inf')
import math
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
9 10
5 3
7 1
5 4
8 7
6 3
5 2
3 0
1 8
0 4
6 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・単純無向グラフ
→連結しているとは限らないことに要注意!

<ポイント>
・二部グラフ判定
・連結でないグラフの二部グラフ判定は、各頂点ごとにbfsを行う必要があるが、すでに
調べた部分はスキップしないと計算量がO(N(N+M))となってしまうのに注意する必要がある
・bfsの際、探索していないところは白→黒→白で塗っていって、探索しているところは隣同士の
色が同じ場合があれば、条件を満たしていないことになる

"""
#--------------------------------------------------------------
N,M = MAP()
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = MAP()
    G[a].append(b)
    G[b].append(a)
 
color = [-1]*N
flag = True
for i in range(N):
    if color[i] == -1:
        color[i] = 0
        que = deque([i])
        while que:
            now = que.popleft()
            for nxt in G[now]:
                if color[nxt]==-1:
                    que.append(nxt)
                    color[nxt] = 1 if color[now]==0 else 0
                else:
                    if color[nxt] == color[now]:
                        flag = False
YesNo(flag)
                           
                    
    