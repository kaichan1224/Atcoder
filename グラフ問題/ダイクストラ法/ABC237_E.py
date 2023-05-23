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
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
4 4
10 8 12 5
1 2
1 3
2 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
重み付きグラフ
標高の差の絶対値の分だけ、楽しさが増・減する
基本的には標高が高いところに行きたい
同じ場所を行って帰る(=二度通るのは)と良くない
楽しさを最大化⇔不快さを最小化
ダイクストラでできることは最短経路なので最小化しかできない
→楽しさの-1倍したものを考えることで最短経路問題へ
ダイクストラはO(Nlog(N))
ベルマンフォードはO(NM)(負のコストも扱えるが計算量が増える:今回はこの場合だとTLE)

<難しいポイント>
・求めたいのは楽しさの最大値
→不快度が最短のものを探す(最小値問題へ置き換える)
・しかし、負の値が出てしまうのでダイクストラは使えない
→楽しさ＋標高を重みにする
・具体的には、、、
低→高のとき楽しさ-2|Hx-Hy|,標高は +|Hx-hy|→総和は-1|Hx-Hy|
高→低のとき楽しさ+|Hx-hy|,標高は-|Hx-Hy|→総和は0
よって、(楽しさ+標高)*-1を重みとして最短経路を求めれば良い
・復元する際は、求めたものd=(-楽しさ-標高)より楽しさ=-d-標高で求められる
・ダイクストラの初期値に注意する→(-楽しさ-標高)が初期値なので,
最初は楽しさ0から始まるので-標高[0]を初期値とする

<応用>
ポテンシャルのお話
負の重みがあるときはベルマンフォードじゃないとだめか?
→解決方法1:重みを捉え直して0以上にする(今回)
→解決方法2:一回だけ最短経路を求めるときはベルマンフォードを使うしかないが
          複数回使うときは、最初だけベルマンフォードをして残りはダイクストラでよい
          (辺の長さを上手いことして正の長さにする)
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
  dist[start] = -H[0] #スタートは0で初期化
  pq = [(-H[0],start)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている

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
H = LIST()
G = [[] for _ in range(N)]
for _ in range(M):
    u,v = MAP()
    u,v = u-1,v-1
    G[u].append((v,max(0,H[v]-H[u])))
    G[v].append((u,max(0,H[u]-H[v])))
d = dijkstra(G,0)
ans = max(-d[i]-H[i] for i in range(N))
print(ans)





