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
2
1 1 3 4
3 4 6 5
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
二次元にもす法
区間の重なる領域を前処理をすることでO(N+HW)で可能に！

注意:前処理は+=1,-=1であることに注意(=1,=-1にしてた(謎))
"""
######################################################
N = INT()
grid = [[0]*1005 for _ in range(1005)]
for _ in range(N):
    lx,ly,rx,ry = MAP()
    #ここの前処理ミスってた(アホ)
    grid[ly][lx] += 1
    grid[ly][rx] -=1
    grid[ry][rx] += 1
    grid[ry][lx] -=1

for x in range(1004):
    for y in range(1004):
        grid[y][x+1] += grid[y][x]

for x in range(1004):
    for y in range(1004):
        grid[y+1][x] += grid[y][x]

cnt = [0]*(N+1)

for x in range(1004):
    for y in range(1004):
        cnt[grid[y][x]] += 1

for k in range(1,N+1):
    print(cnt[k])




