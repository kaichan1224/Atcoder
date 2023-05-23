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
3 5
5
1 2 3 4 5

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・最短経路絡みの問題以外は基本dfs

"""
#--------------------------------------------------------------
H,W = MAP()
N = INT()
A = LIST()
grid = [[-1]*W for i in range(H)]
grid[0][0] = 1
que = deque()
que.append([0,0,1])
d = [0]*N
d[0] += 1
while que:
    y,x,color = que.popleft()
    if d[color-1]>=A[color-1]:
        color += 1
    for dy,dx in dirc:
        if color==N+1:
            break
        ny,nx = y+dy,x+dx
        if not (0<=ny<H and 0<=nx<W):
            continue
        if grid[ny][nx]==-1:
            grid[ny][nx] = color
            d[color-1] += 1
            que.append([ny,nx,color])
for y in range(H):
    for x in range(W):
        print(grid[y][x],end=' ')
    print()


    





