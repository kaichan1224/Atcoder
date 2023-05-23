import io
import sys
import math
#sys.setrecursionlimit(10**7) #再帰呼び出し
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
mod = 998244353
#-----------------------------------------------------
_INPUT = """\
3 2
1 2 3
2 3 2
"""
sys.stdin = io.StringIO(_INPUT)
#-----------------------------------------------------
"""
<考察>
O(N^3)でちょうど間に合う
f(s,t,k)をO(1)で求めたい→前処理必要?
Ci>0よりダイクストラ?
→全ての点の間の距離なのでワーシャルフロイド

<本質的な理解>
* 有向・無向グラフ両方で使用可能
* ある頂点から移動可能なすべての頂点への移動コストを２次元リストで表現
* 使える中継点を一番小さい頂点から順番に見ていき、始点から終点までの
距離を、中継点を使う場合と使わない場合の最小値で更新することで
O(N^3)で求めることができる
"""
#-----------------------------------------------------
INF = float('inf')
N,M = map(int,input().split())    # Nは頂点数、Mは辺数
# d[u][v]は辺e=(u,v)のコスト
# (存在しない場合はINF、ただしd[i][i]=0とする)
d = [[INF] * N for _ in range(N)]#最初は辺が存在しないと仮定して全てINFで埋める
for i in range(N):#始点と終点が同じ場合は0
    d[i][i] = 0
for _ in range(M):
    s, t, c = map(int,input().split())
    s,t = s-1,t-1
    d[s][t] = c #s→tは辺が存在する(当たり前)ので重みをそもまま入れる

def warshall_floyd():
    for k in range(N):#経由する頂点
        for i in range(N):#始点
            for j in range(N):#終点
                #頂点kを経由した場合の最短経路を求める
                #頂点i→頂点j = min(頂点i→頂点j ,頂点i→頂点k+頂点k→頂点j)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0

def warshall_floyd2():
    global ans
    for k in range(N):#経由する頂点
        for i in range(N):#始点
            for j in range(N):#終点
                #頂点kを経由した場合の最短経路を求める
                #頂点i→頂点j = min(頂点i→頂点j ,頂点i→頂点k+頂点k→頂点j)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        
        for i in range(N):
            for j in range(N):
                if d[i][j]!=INF:
                    ans += d[i][j]

warshall_floyd2()
print(ans)







