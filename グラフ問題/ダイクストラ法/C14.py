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
6 7
1 2 15
1 4 20
2 3 65
2 5 4
3 6 50
4 5 30
5 6 8
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・重みつきグラフの最短経路なので、ダイクストラ法を使えばよさそうだけど、
通る可能性がある点の数を求める必要があるので、bfsの時のように上手く場合分けするか
DPしながらダイクストラ?みたいなことをすればいいのでは.

・経路復元しながらbfsでもいいかもしれない(後ろからDP)
・問題を誤読していました。
・求めるのは、経路が何通りあるかではなく、通りうる頂点の個数でした。
・一度経路を求めてからありうるものをsetに格納していけば良さげ?

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M = MAP()
G = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
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

dist = dijkstra(G,0)
ans = [0]*N
ans[N-1] = 1
que = deque([N-1])
s = set()
s.add(N)
while que:
    now = que.popleft()
    for nxt,cost in G[now]:
        if dist[nxt]==dist[now]-cost:
            que.append(nxt)
            s.add(nxt+1)
print(len(s))
