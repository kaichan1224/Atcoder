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
3 3
1 2 70 1
2 3 20 1
1 3 90 0
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・拡張ダイクストラっぽい?
dist[頂点][本数]:dist[n][0]
→全然違う
・必ず行き来できる
・一旦bfsで書いてみる?
・N=8000なのでNlogNじゃないとだめ!
→優先度つきキューのダイクストラで。
・お気持ちとしては複数条件で要素を取り出したい
↓
・ダイクストラ内部を色々工夫したら残り2WAまではきた
・遷移を改善したらAC!

<キーワード>
・ダイクストラ

<ポイント>
・同じコストが最小のものの中で木が多い経路を通りたい
→木を僅かなボーナスと捉える
・普通のコストは整数値であるため、木がある経路のところはコストを-0.0001する
ことにより、同じコストの場合の差別化とコスト最小化を両方実現することができる
・少数だと誤差が心配なので整数値にしておくと安心。

"""
#--------------------------------------------------------------
N,M = MAP()
#(繋がる頂点、重み、木の有無)
G = [[] for _ in range(N)]
for _ in range(M):
    a,b,c,d = MAP()
    a,b = a-1,b-1
    c = 10000*c
    if d==1:
        G[a].append((b,c-1))
        G[b].append((a,c-1))
    else:
        G[a].append((b,c))
        G[b].append((a,c))

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

def dijkstra2(G,start):
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
  cnt = [-1]*N
  cnt[start] = 0
  
  #スタート地点の重み（距離）
  dist[start] = 0 #スタートは0で初期化
  pq = [(0,start,0)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている
  while pq:
    #ヒープから取り出し
    cost,v,ki = heappop(pq)
    if dist[v] != cost: continue
    #最もコストが小さい頂点を探す
    for v,d,k in G[v]:#G[u]にはつながっている頂点番号とそこへのコストが入っている
      new_cost = cost + d
      #更新条件
      if dist[v] >= new_cost: 
        dist[v] = new_cost
        cnt[v] = max(cnt[v],ki+k)
        heappush(pq,(new_cost,v,cnt[v])) #pqに(new_cost,v)
  return dist,cnt

dist = dijkstra(G,0)
true_num = 10000-dist[N-1]%10000
print((dist[N-1]+true_num)//10000,true_num)

    
    
    