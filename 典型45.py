import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<bitDP>
->集合に対するDP,N個の要素の順列の中で最適なものを求めたいときに使う
・O(N*N!)->O(N**2*2**N)程度に改善.(N=10->N=19ぐらい)
・DP[S][v]:集合の全体のうちの部分集合Sの順列の中でvが末端となるものうち最適なもの
・集合を配列の添字として設定できないので、整数で考える必要がある.
・集合は順列ではないことに注意!->末端(現在地)だけ特別視している
・考えうる集合の個数はあるなしの2択がN個あることを考えると、2**N通りある
・どこの頂点(v)からどこの頂点(u)へ移動するという情報が欲しい
Sの末端がv->(S+u)の集合という風に考えれば良い

<部分集合の部分集合>
・部分集合から別の部分集合に遷移し、かつ遷移が集合が大きくなる方向に限定されるような時
・
"""
#-------------------------------
N,K = MAP()
XY = [LIST() for _ in range(N)]
#全てのペアの２頂点間の距離
dist = [[0]*N for _ in range(N)]
for i in range(N):
    x0,y0 = XY[i]
    for j in range(i):
        x1,y1 = XY[j]
        d = (x0-x1)**2+(y0-y1)**2
        dist[i][j] = dist[j][i] = d



