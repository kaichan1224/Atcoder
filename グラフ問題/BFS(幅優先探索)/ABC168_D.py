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
6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
グラフ問題のアプローチ
DFS,BFS,etc:更新の仕方   DP:状態の持ち方

BFS:最小手が関係するとき
DFS:それ以外(根からの距離、頂点にたどり着けるか判定、連結成分個数
    二部グラフ判定、閉路検出、他にもたくさん)
"""
######################################################
N,M = MAP()
G = [[] for _ in range(N)]
for _ in range(M):
    a,b =MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

ans = [-1]*N
dist = [-1]*N
dist[0] = 0
que = deque([0])
route = [-1]*N
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]==-1:
            dist[nxt] = dist[now]+1
            route[nxt] = now+1
            que.append(nxt)
flag = True            
for i in range(1,N):
    if route[i]==-1:
        flag = False
if flag:
    print('Yes')
    for i in range(1,N):
        print(route[i])
else:
    print('No')
    

