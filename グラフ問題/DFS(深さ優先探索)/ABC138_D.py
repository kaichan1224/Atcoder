import io
import sys
#sys.setrecursionlimit(10**7)
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
6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
木上でいもす法
頂点p[j]にx[j]を足した状態で、根からある頂点の値を子に足していくと
部分木すべてに+x[j]を伝播させることが出来る
期限がないので終点に-する必要がない
"""
######################################################
N,Q = MAP()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

ans = [0]*N
for _ in range(Q):
    p,x = MAP()
    p -= 1
    ans[p] += x
#print(ans)
def dfs(v,pre):
    for u in G[v]:
        if u!=pre:
            ans[u] += ans[v]
            dfs(u,v)
dfs(0,-1)
print(*ans)





