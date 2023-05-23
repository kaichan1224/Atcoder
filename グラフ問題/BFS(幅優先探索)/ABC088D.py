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
10 37
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
.....................................
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
・ただの幅優先探索
・条件を満たさない場合に-1出力するのを忘れないように
"""
#--------------------------------------------------------------
H,W = MAP()
grid = [list(input()) for i in range(H)]
q = deque()
q.append([0,0])
dist = [[-1]*W for i in range(H)]
dist[0][0] = 1
cnt = 0
for y in range(H):
    for x in range(W):
        if grid[y][x]=='.':
            cnt += 1
while q:
    y,x = q.popleft()
    for dy,dx in dirc:
        ny,nx = y+dy,x+dx
        if not (0<=ny<H and 0<=nx<W):
            continue
        if dist[ny][nx]==-1 and grid[ny][nx]=='.':
            q.append([ny,nx])
            dist[ny][nx] = dist[y][x] + 1
if dist[H-1][W-1]==-1:
    print(-1)
else:
    print(cnt-dist[H-1][W-1])





