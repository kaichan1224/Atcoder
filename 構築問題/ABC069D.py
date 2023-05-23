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
・色はN種類あり、iのマスはちょうどai個存在する
・N=10^4,H=100,W=100
・各色のマスは上下左右に連結
・角マス愚直に実装していけば良いのでは

<キーワード>

<ポイント>
・条件を満たしていくように当てはめていく問題
・複数回答があるような場合には、簡単に条件を満たすパターンを考えると楽に実装できるかもしれない
"""
#--------------------------------------------------------------
H,W = MAP()
N = INT()
A = LIST()
grid = []
now = N
for h in range(H):
    tmp = []*W
    for w in range(W):
        if A[-1]>1:
            A[-1] -= 1
            tmp.append(now)
        else:
            A.pop()
            tmp.append(now)
            now -= 1
    if h%2==1:
        tmp.reverse()
    grid.append(tmp)

for h in range(H):
    for w in range(W):
        print(grid[h][w],end=" ")
    print()