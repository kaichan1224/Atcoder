import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))  #距離の管理
INF = float('inf')
_INPUT = """\
3 3
1 2
1 3 3
3 2 3
1 2 1
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
・両側からダイクストラするだけ.
・dist[i]==INFの時のコーナーケースに注意する.
"""
#-------------------------------
N,M = MAP()
S,T = MAP()
S,T = S-1,T-1
G = [[] for _ in range(N)]
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
for _ in range(M):
    x,y,d = MAP()
    x,y = x-1,y-1
    G[x].append((y,d))
    G[y].append((x,d))

distS = dijkstra(G,S)
distT = dijkstra(G,T)

for i in range(N):
    if i==S or i==T:
        continue
    if distS[i]==distT[i] and distS[i]!=INF and distT[i]!=INF:
        print(i+1)
        exit()
print(-1)








