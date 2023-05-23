import heapq
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
#--------------------------------------------------------------
_INPUT = """\
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<A*アルゴリズムで迷路を解く>
・スタートからゴールへの最短距離をf(n),スタートからノードnまでの最短距離をg(n),
ノードnからゴールまでの最短距離をh(n)とすると、
f(n) = g(n) + h(n)
・g(n),h(n)がわかっていたら当然苦労しないわけで暫定的な値を用いる
・g(n):スタートからノードnまでの最短距離予測で、今まで辿ってきた経路を覚えていればなんとかなる
・h(n):ゴールに辿り着くまで分からない->人間が設計した推定値を与える
-マンハッタン距離やユークリッド距離を用いる

<+α>
・応用として、地形コストを考慮した経路も考えることができる
・他にも敵の視野に入っているノードはコストが高いとして、組み込む影響マッピングなどもある
"""
#--------------------------------------------------------------    
def manhattan_distance(nowy,nowx,nxty,nxtx):
    return abs(nowy-nxty)+abs(nowx-nxtx)
    
H,W = MAP()
sy,sx = MAP()
sy,sx = sy-1,sx-1
gy,gx = MAP()
gy,gx = gy-1,gx-1
grid = [list(input()) for _ in range(H)]
dist = [[INF]*W for _ in range(H)]#スタート地点以外の値は∞で初期化
weight = [[INF]*W for _ in range(W)]#dist+h(x)

dist[sy][sx] = 0 #スタートは0で初期化
weight[sy][sx] = dist[sy][sx]+manhattan_distance(sy,sx,gy,gx)#ヒューリスティックな重み付き
pq = [(weight[sy][sx],sy,sx)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている

while pq:
    cost,nowy,nowx = heappop(pq)
    if gy == nowy and gx == nowx:
        break
    for dy,dx in dirc:
        nxty,nxtx = nowy+dy,nowx+dx
        if not (0<=nxty<H and 0<=nxtx<W):
            continue
        if grid[nxty][nxtx]=="#":
            continue
        dist[nxty][nxtx] = min(dist[nowy][nowx] + 1,dist[nxty][nxtx])
        newcost = dist[nxty][nxtx] + manhattan_distance(nxty,nxtx,gy,gx)
        if weight[nxty][nxtx] > newcost:
            weight[nxty][nxtx] = newcost
            heappush(pq,(newcost,nxty,nxtx))
print(dist[gy][gx])