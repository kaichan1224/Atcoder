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
5 5
1 2 12
2 3 14
3 4 7
4 5 9
5 1 18



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・高々往復する路線は１つ→木?
・頂点数Nの成約が小さい→ダイクストラで全ての頂点について全探索しても間に合いそう
→全点間だからワーシャルフロイドで良くね
"""
#--------------------------------------------------------------
def dijkstra(G,start):
    """
    ダイクストラ法(優先度付きキュー使用)
    from heapq import heappop,heappushの使用を忘れずに！
    引数：グラフ（重み付き）、スタート地点
    返り値：頂点の個数分の配列を返し、スタートから配列のindexまでの最短距離を求めることが出来る
    """
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

N,M = MAP()
G = [[] for _ in range(N)]
d = defaultdict(list)
for i in range(M):
    a,b,t = MAP()
    a,b = a-1,b-1
    G[a].append((b,t))
    G[b].append((a,t))
ans = INF
for i in range(N):
    d = dijkstra(G,i)
    ans = min(ans,max(d))
print(ans)











