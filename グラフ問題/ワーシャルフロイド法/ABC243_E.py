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
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
3 3
1 2 2
2 3 3
1 3 6
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
*最小全域木なら条件を満たす?→s-tが全て一致なので多分違う
*O(N^3)まで間に合う
*s-t間の距離が変わってはいけない
*頂点kを経由した場合とそうでない場合に、最短経路が変わらなければよい

<ポイント>
*辺を格納する
*無向グラフなので双方向に重みを書くのを忘れずに
*各辺に迂回路があるかの問題
→各辺についてd(a,b)<=cならその辺は不要と判断することができる
*関数定義するだけで満足してるアホいる？いねえよな？？

"""
#--------------------------------------------------------------
INF = float('inf')
N,M = MAP()   # Nは頂点数、Mは辺数
es = []
# d[u][v]は辺e=(u,v)のコスト
# (存在しない場合はINF、ただしd[i][i]=0とする)
d = [[INF]* N for _ in range(N)]#最初は辺が存在しないと仮定して全てINFで埋める
#for i in range(N):#始点と終点が同じ場合は0
    #d[i][i] = 0
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    es.append((a,b,c))
    d[a][b] = c #s→tは辺が存在する(当たり前)ので重みをそもまま入れる
    d[b][a] = c #逆向き貼り忘れに注意！！！
def warshall_floyd():
    for k in range(N):#経由する頂点
        for i in range(N):#始点
            for j in range(N):#終点 
                #頂点kを経由した場合の最短経路を求める
                #頂点i→頂点j = min(頂点i→頂点j ,頂点i→頂点k+頂点k→頂点j)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
warshall_floyd()
cnt = 0
#全ての辺について、
for a,b,c in es:
    #a,bが使えない場合を考えれば良い
    unused = 0
    #迂回路がある場合、その辺は使わなくて良い
    for k in range(N):
        if d[a][k]+d[k][b]<=c:
            unused += 1
    cnt += unused
print(cnt)








