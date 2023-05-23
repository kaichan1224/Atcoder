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
4
0 0
0 1
1 0
1 1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
<キーワード>
・bitDPとは?
->集合に対するDP,N個の要素の順列の中で最適なものを求めたいときに使う
・O(N*N!)->O(N**2*2**N)程度に改善.(N=10->N=19ぐらい)
・DP[S][v]:集合の全体のうちの部分集合Sの順列の中でvが末端となるものうち最適なもの
・集合を配列の添字として設定できないので、整数で考える必要がある.
・集合は順列ではないことに注意!->末端(現在地)だけ特別視している
・考えうる集合の個数はあるなしの2択がN個あることを考えると、2**N通りある
・どこの頂点(v)からどこの頂点(u)へ移動するという情報が欲しい
Sの末端がv->(S+u)の集合という風に考えれば良い

<ポイント>
・循環セールスマン問題をbitDPで解くときのTIPS
dp[S][j]:既に訪問した都市の集合がSで現在位置がjである時の、現時点での最小移動距離
・使うbit演算
・1<<N:2**Nのこと
・n>>k & 1:nのk+1桁目が1かどうか(0-indexedなら右からk番目)
・S&T 集合の積
・通った都市(集合S)に今いる都市は含まれていることに注意!!

更新式は、頂点 u から v までの距離を cost(u,v) とすると以下の通りとなります。
dp[S U {v}][v] = min(dp[S][u]+cost(u,v))
・S!=0つまり最初どの頂点も訪れていないときは例外的に処理しないとダメ!!!!
"""
#--------------------------------------------------------------
N = INT()
XY = [LIST() for _ in range(N)]
def f(i,j):
    return math.sqrt((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)

#dp[S][i]:既に訪問した都市の集合がSで現在位置がiの時の答え(最小値)
dp = [[INF]*(N) for _ in range(2**(N))]
dp[0][0] = 0
for S in range(2**N):#集合
    for v in range(N):#Sの末端
        if (S>>v & 1) == 0 and S!=0:#S=0の場合は例外?
            continue
        for u in range(N):#現在地(v->uへ移動する)
            if (S >> u & 1) == 0:#配るDP,Sが
                dp[S|(1<<u)][u] = min(dp[S|(1<<u)][u],dp[S][v]+f(v,u))
print(dp[2**N-1][0])
