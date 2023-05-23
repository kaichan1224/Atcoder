import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float("inf")
_INPUT = """\
5 4
1 2 1
1 3 1
1 4 1
1 5 1

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
・行って帰ってくる道のうち、最短距離のもの
・dfsだとTLEした。(O(V+E)?? V=300,M=300*299=~10**5なので行けるのでは??)
・木じゃないグラフのdfsは計算量やばそう
・同じ道を通らないといけない、一つ以上は通る必要がある

<ポイント>
・0->u->(....)->v->0の最短経路を分けて考えれば良い。
・0->u,v->0は隣接点同士で、u->vは全頂点間の最短経路をワーシャルフロイドでO(N^3)で求めれば良い
・その時にワーシャルフロイドは0を通らないようなものにする必要があることに注意!
・なおu!=v
"""
#-------------------------------
N,M = MAP()
distfor0 = [INF]*N
dist = [[INF]*N for _ in range(N)]#最初は辺が存在しないと仮定して全てINFで埋める
for i in range(N):#始点と終点が同じ場合は0
    dist[i][i] = 0
for _ in range(M):
    u,v,l = MAP()
    u,v = u-1,v-1
    if u==0:
        distfor0[v] = l
    else:
        dist[u][v] = l
        dist[v][u] = l

def warshall_floyd():
    #kを1番外側でループさせることで、一度のループで最短経路を計算できるようにする
    for k in range(N):#経由する頂点 中継点を1番外のループにする
        for i in range(N):#始点
            for j in range(N):#終点
                #頂点kを経由した場合の最短経路を求める
                #頂点i→頂点j = min(頂点i→頂点j ,頂点i→頂点k+頂点k→頂点j)
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

warshall_floyd()
ans = INF
for u in range(N):
    for v in range(N):
        if u!=v:
            ans = min(ans,distfor0[u]+distfor0[v]+dist[u][v])
print(ans if ans!=INF else -1)






