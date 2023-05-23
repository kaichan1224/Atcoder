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
5 6 2
6 5 9 15 3
4 2
1 5
2 5
2 4
1 3
4 3
2 1
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
この問題も、グラフを逆向きに貼ってゴール始点の幅優先探索をする問題
多点始点幅優先探索の場合、一点始点の幅優先探索と同じ用に、
始点すべてをqueにappendしてよい
同じ場所を2度以上appendしない用に注意する
"""
######################################################
N,M,K = MAP()
H = LIST()
C = LIST()
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = MAP()
    a,b=a-1,b-1
    if H[a]>H[b]:
        G[a].append(b)
    else:
        G[b].append(a)

can_stop = [False]*N
for c in C:
    can_stop[c-1] = True

#まずは愚直実装
for i in range(N):
    que = deque([i])
    dist = [-1]*N
    dist[i] = 0
    flag = False
    while que:
        now = que.popleft()
        if can_stop[now]:
            flag = True
            print(dist[now])
            break
        for nxt in G[now]:
            if dist[nxt]==-1:
                que.append(nxt)
                dist[nxt] = dist[now]+1
    if flag==False:
        print(-1)




