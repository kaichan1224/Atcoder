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
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
4 4
1 1
4 4
..#.
..#.
.#..
.#..

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・移動手段は
1.上下左右 2.今いる位置から+-2の範囲にワープの2種類
・一旦BFSを考える
→01BFSで行けそう

<メモ>
・計算量のお話
ダイクストラ:優先度付きキューO(V+ElogV)
幅優先探索:キュー使用　O(V+E)
01-BFS:両端キュー (V+E)

・01BFSはdistの初期値をINFにする必要があるので注意!!!
"""
#--------------------------------------------------------------
H,W = MAP()
Ch,Cw = MAP()
Dh,Dw = MAP()
Ch,Cw,Dh,Dw = Ch-1,Cw-1,Dh-1,Dw-1
grid = [list(input()) for _ in range(H)]
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
dist = [[INF]*W for _ in range(H)]
#ワープ回数をメモする
dist[Ch][Cw] = 0
que = deque()
que.append((Ch,Cw))
while que:
    nowy,nowx  = que.popleft()
    #移動方法1つ目
    for dy,dx in dirc:
        nxty,nxtx = nowy+dy,nowx+dx
        if not (0<=nxty<H and 0<=nxtx<W):
            continue
        if grid[nxty][nxtx] == "#":
            continue
        if dist[nxty][nxtx] > dist[nowy][nowx]:
            dist[nxty][nxtx] = dist[nowy][nowx]
            que.appendleft((nxty,nxtx))#コスト0

    #移動方法2つ目
    for dy in range(-2,3):
        for dx in range(-2,3):
            nxty,nxtx = nowy+dy,nowx+dx
            if not (0<=nxty<H and 0<=nxtx<W):
                continue
            if grid[nxty][nxtx] == "#":
                continue
            if dist[nxty][nxtx] >dist[nowy][nowx]+1:
                que.append((nxty,nxtx))
                dist[nxty][nxtx] = dist[nowy][nowx] + 1
print(dist[Dh][Dw])


















