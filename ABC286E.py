import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
5
30 50 70 20 60
NYYNN
NNYNN
NNNYY
YNNNN
YNNNN
3
1 3
3 1
4 5




"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
N = INT()
A = LIST()
path = [list(input()) for _ in range(N)]
Q = INT()
INF = float("inf")
dist = [[INF]*N for _ in range(N)]#最初は辺が存在しないと仮定して全てINFで埋める
cost = [[INF]*N for _ in range(N)]
for i in range(N):#始点と終点が同じ場合は0
    cost[i][i] = 0
for s in range(N):
    for t in range(N):
        if s==t:
            continue
        if path[s][t]=="Y":
            cost[s][t] = 1
            dist[s][t] = -A[t]

def warshall_floyd():
    #kを1番外側でループさせることで、一度のループで最短経路を計算できるようにする
    for k in range(N):#経由する頂点 中継点を1番外のループにする
        for i in range(N):#始点
            for j in range(N):#終点
                #頂点kを経由した場合の最短経路を求める
                #頂点i→頂点j = min(頂点i→頂点j ,頂点i→頂点k+頂点k→頂点j)
                if cost[i][j]>cost[i][k]+cost[k][j]:#kを経由するときに
                    cost[i][j] = cost[i][k] + cost[k][j]
                    dist[i][j] = dist[i][k] + dist[k][j]
                elif cost[i][j] == cost[i][k]+cost[k][j] and dist[i][j] > dist[i][k]+dist[k][j]:#kを経由しない方がいいなら
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

warshall_floyd()
for _ in range(Q):
    u,v = MAP()
    u,v = u-1,v-1
    if cost[u][v]==INF:
        print("Impossible")
    else:
        print(cost[u][v],-dist[u][v]+A[u])





