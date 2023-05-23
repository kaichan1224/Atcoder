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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
7 9
1 2 2
1 3 3
2 5 2
3 4 1
3 5 4
4 7 5
5 6 1
5 7 6
6 7 3
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
ダイクストラの基本問題
計算量はO(NlogN)
重み付きグラフにおいて、
開始点からの全ての点への距離を求めることが出来る
"""
######################################################
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
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    G[a].append((b,c))
    G[b].append((a,c))

d1 = dijkstra(G,0)
d2 = dijkstra(G,N-1)
for k in range(N):
    print(d1[k]+d2[k]) 