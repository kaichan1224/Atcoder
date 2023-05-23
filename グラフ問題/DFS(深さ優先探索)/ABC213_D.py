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
4
1 2
4 2
3 1
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
オイラーツアー:DFSで探索した頂点をメモして配列にするだけ
頂点に注目するものと、辺に注目するものの2種類ある
(今回の問題では頂点に注目した問題)

頂点に注目:頂点が初めて探索されたときと、子の一つが探索し終わったとき
辺に注目:(上から下に行く辺は+下の頂点、下から上に行く辺は-下の頂点)
頂点が初めて探索されるときに+(頂点)を配列に追加、
頂点を探索し終えたときに-(頂点)を配列に追加する
"""
######################################################
N = INT()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
for i in range(N):
    G[i].sort()
print(G)
ans = []
def dfs(v,pre):
    #頂点が初めて探索されるタイミング(行きがけ)
    ans.append(v+1)
    for u in G[v]:
        if u!=pre:
            dfs(u,v)
            #子の一つが探索終わったタイミング
            ans.append(v+1)
    #頂点が探索終えたタイミング(帰りがけ)        
dfs(0,-1)    
print(ans)
    


