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
2 4
0 9 9 9 9 9 9 9 9 9
9 0 9 9 9 9 9 9 9 9
9 9 0 9 9 9 9 9 9 9
9 9 9 0 9 9 9 9 9 9
9 9 9 9 0 9 9 9 9 2
9 9 9 9 9 0 9 9 9 9
9 9 9 9 9 9 0 9 9 9
9 9 9 9 9 9 9 0 9 9
9 9 9 9 2 9 9 9 0 9
9 2 9 9 9 9 9 9 9 0
-1 -1 -1 -1
8 1 1 8
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・0<=n<=9 から1にするまでにかかる魔力の最少量のそれぞれ求める
→重み付きグラフの最小経路なのでダイクストラ?

<ポイント>
・ワーシャルフロイドで一発です
"""
#--------------------------------------------------------------
def dijkstra(G,start):
    N = len(G)
    #距離の管理
    INF = float('inf')
    dist = [INF]*N #スタート地点以外の値は∞で初期化
    #スタート地点の重み（距離）
    dist[start] = 0 #スタートは0で初期化
    pq = [(0,start)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている
    while pq:
    #ヒープから取り出し
        cost,v = heappop(pq)
        if dist[v] != cost: continue
        #最もコストが小さい頂点を探す
        for v,d in G[v]:#G[u]にはつながっている頂点番号とそこへのコストが入っている
            new_cost = cost + d
            #更新条件
            if dist[v] > new_cost: 
                dist[v] = new_cost
                heappush(pq,(new_cost,v)) #pqに(new_cost,v)
    return dist

H,W = MAP()
c = [LIST() for i in range(10)]
a = [LIST() for i in range(H)]
G = [[] for i in range(10)]
#変える必要のある数の個数
d = defaultdict(int)
for h in range(H):
    for w in range(W):
        if a[h][w]==1 or a[h][w]==-1:
            continue
        else:
            d[a[h][w]] += 1

for s in range(10):
    for g in range(10):
        G[s].append((g,c[s][g]))
    
minmaho = [0]*10
for i in range(10):
    dist = dijkstra(G,i)    
    minmaho[i] = dist[1]
ans = 0
for k,i in d.items():
    ans += minmaho[k]*i
print(ans)








