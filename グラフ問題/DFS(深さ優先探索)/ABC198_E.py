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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
考察
*木の問題でO(NlogN)なら間に合うのでLCAも選択肢にあり
*探索している時点で、頂点1と同じ数字があったらそれ以降の頂点はout
*一回の探索dfsで行けそう
*最短経路絡みなのでbfsで解ける？かも
*usedリストはそれぞれのパスでのものなので全体で使うのはだめ
*木だしやっぱりdfsかも
"""
######################################################
N = INT()
C = LIST()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
ans = []
d = defaultdict(int)
def dfs(v,pre):
    d[C[v]] += 1
    if d[C[v]]<2:
        ans.append(v+1)
    for u in G[v]:
        if u!=pre:
            dfs(u,v)
    d[C[v]] -= 1
dfs(0,-1)
ans.sort()
for a in ans:
    print(a)



