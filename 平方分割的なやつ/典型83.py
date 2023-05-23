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
4 4
1 2
1 3
1 4
2 3
5
4 2
3 3
2 4
4 5
1 6
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
・連結な単純無向グラフ
・今いる点と隣接する点の色を書き換える部分がボトルネック
→どうやって解消すればいいのか=平方分割でゴリ押す

<平方分割>
・N個の列を√N程度の大きさのバケットに分けて管理

<問題のポイント>
・どのように工夫するか
->大きい次数を塗るのを遅延させる
rtM未満
    - 隣接全部塗り替え
以上
    - 記録するだけ
    - ただし、隣接する次数rtM以上の頂点に直近の塗り替えがないかを調べる必要がある
"""
#-------------------------------
N,M = MAP()
G = [[] for _ in range(N)]
higherG = [[] for _ in range(N)]
color = [(1,-1)]*N #(color,query)
lazy = [(1,-2)]*N #(color,query)
rtM = int(M**0.5)
for _ in range(M):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

#辺の数がrtM以上のもののグラフを考える
for i in range(N):
    for v in G[i]:
        if len(G[v])>=rtM:
            higherG[i].append(v)
Q = INT()
for i in range(Q):
    x,y = MAP()
    x = x-1
    #xにつながっている次数d以上の頂点に直近の塗り替えがないかを調べる
    for v in higherG[x]:
        #x,vのindexに注意!!!
        if color[x][1] <lazy[v][1]:#遅延用のデータのクエリの方が最新だったら更新
            color[x] = lazy[v]

    print(color[x][0])
    color[x] = (y,i)
    #辺の数がrtM未満だったら愚直に実装する(しても計算量は大きくはならない)
    if len(G[x])<rtM:
        color[x] = (y,i)
        for v in G[x]:
            color[v] = (y,i)
    #辺の数がrtM以上だったら愚直に実装
    else:
        lazy[x] = (y,i)


    


