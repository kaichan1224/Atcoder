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
10 5


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・操作回数の最小値->bfsで解けます(ネタバレ食らってたけど)

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,M = MAP()
dist = [[-1]*(N+1) for _ in range(N+1)]
dist[1][1] = 0
que = deque()
que.append([1,1])
while que:
    nowy,nowx = que.popleft()
    #ちょうどルートMであるマスを列挙するかつ未探索だったら
    #YについてはルートMの範囲のみを調べればよく
    for x in range(-N,N+1):
        y2 = M-x**2
        if y2<0:
            continue
        y = math.sqrt(y2)
        if not y.is_integer():
            continue
        y = int(y)
        x = int(x)
        dirc = [(-x,y),(-x,-y),(x,y),(x,-y)]
        for dx,dy in dirc:
            nxtx = nowx + dx
            nxty = nowy + dy
            if 1<=nxtx<=N and 1<=nxty<=N:
                if dist[nxty][nxtx] == -1:
                    dist[nxty][nxtx] = dist[nowy][nowx] + 1
                    que.append((nxty,nxtx))
for y in range(1,N+1):
    for x in range(1,N+1):
        print(dist[y][x],end=" ")
    print()

