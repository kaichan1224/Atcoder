from cmath import inf
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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
2 3 10
S##
.#G
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
迷路の最短経路なので幅優先探索
答えでにぶちゃん

<ポイント>
迷路の位置によってかかる時間が変わる→重み付きの迷路
よって幅優先探索では解くことができず、dfsで経路全探索(時間かかる)
でも解けるが計算量が大きくなってしまう
→ダイクストラ
"""
#--------------------------------------------------------------
H,W,T = MAP()
grid = [list(input()) for i in range(H)]
for h in range(H):
    for w in range(W):
        if grid[h][w]=='S':
            sy,sx = h,w
        if grid[h][w]=='G':
            gy,gx = h,w
#めぐる式二分探索
def is_ok(arg):
    pq = [(0,sy,sx)]
    dist = [[INF]*W for i in range(H)]
    dist[sy][sx] = 0
    while pq:
        cost,y,x= heappop(pq)
        for dy,dx in dirc:
            ny,nx = y+dy,x+dx
            if not(0<=ny<H and 0<=nx<W):
                continue
            if grid[ny][nx]=='.' or grid[ny][nx]=='G':
                newcost = cost + 1
            elif grid[ny][nx]=='#':
                newcost = cost + arg
            if dist[ny][nx] > newcost:
                dist[ny][nx] = newcost
                heappush(pq,(newcost,ny,nx)) 
    return dist[gy][gx]<=T

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(T,0))


