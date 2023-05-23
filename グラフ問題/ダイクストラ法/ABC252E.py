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
4 6
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1
3 4 1


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・最小全域木をいい感じに調整する

<ポイント>
・都市 1 から都市 i の最短経路において、都市 i に到達する直前に使った道路」をそれぞれ残せば十分

<最小全域木と最短経路木>
・二つは似てるようで全然違います!!!!!
・最小全域木はufとソート、最短経路木はダイクストラするだけです
・最短路木:根を持ち有向,最小全域:根を持たず無向
・最小全域木：一つだけ存在、・最短路木：start頂点を変えると変化
"""
#--------------------------------------------------------------
def dijkstra(G,start):
    """
    history:使った辺を記録(値が欲しい時ヒャreturnで返す)
    dist:それぞれの頂点への最短距離を返す
    """
    N = len(G)
    #距離の管理
    dist = [INF]*N #スタート地点以外の値は∞で初期化
    history = [0]*N
    #スタート地点の重み（距離）
    dist[start] = 0 #スタートは0で初期化
    pq = [(0,start)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている
    while pq:
        #ヒープから取り出し
        cost,v = heappop(pq)
        if dist[v] != cost: continue
        #最もコストが小さい頂点を探す
        for u,d,idx in G[v]:#G[u]にはつながっている頂点番号とそこへのコストが入っている
            new_cost = cost + d
            #更新条件
            if dist[u] > new_cost: 
                dist[u] = new_cost
                history[u] = idx
                heappush(pq,(new_cost,u)) #pqに(new_cost,v)
    return history

N,M = MAP()
history = [-1]*N
G = [[] for _ in range(N)]
for i in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    G[a].append((b,c,i+1))
    G[b].append((a,c,i+1))

d1 = dijkstra(G,0)
ans = d1[1:]
print(*ans)





