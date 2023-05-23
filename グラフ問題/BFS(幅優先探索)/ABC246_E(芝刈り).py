import io
import sys
import math
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
inf=float('inf')
###################################################
_INPUT = """\
5
1 3
3 5
....#
...#.
.....
.#...
#....
"""
sys.stdin = io.StringIO(_INPUT)
###################################################
"""
01BFS:辺の長さが0または1である有向グラフにおいて、全頂点への最短経路
    の長さを効率時間で求める事ができる

<アルゴリズムにおけるポイント>
・暫定最短距離が最も小さい点を選んでそこから伸びる辺で他の頂点の暫定最短距離
を更新する
・辺の重みが0or1の2つしかない場合、BFSのdequeにおいて0に辺を用いた場合は先頭に、
1の辺を用いた場合は末尾に加えることで処理することが出来る
(この処理により、ある値が前側に、それより1大きいコストが後ろ側に固まっている状態を
保つことが出来る)
・計算量をダイクストラO(V+ElogV)からO(V+E)に落とせる
・ノーコストの手段で移動する、何らかのコストや回数制限のある手段で移動
の2通りの移動方法が与えられているような問題で帰着できる可能性がある

<方向転換の最小化>
・現在向いている方向に1マス進む(コスト0)
・向いている方向を変える(コスト1)
スタート→ゴールを最小にする

解法1(芝刈りBFS解):
今いる地点から進行方向4箇所について、壁に突き当たるor現時点よりもコストが同じ以上
のところについて,同じコストでdistを更新する。その後次にqueの先頭に入っている部分について
また同じ操作をする

解法2(拡張BFS):
辺の頂点に関する状態を拡張して考える.
dist[i][j][0-3]:マスi,jでそれぞれの方向に向く状態までの方向転換の最小回数
(nowx,nowy,直前の移動方向)の3つの組を一つの頂点として01dfs
(nowx,nowy,直前の移動方向)の3つの組を一つの頂点として01dfs

遷移は今向いている向きにコスト0で一回移動
現在のマスから移動せずにコスト1で向いている向きを変更
の2種類

コスト0の遷移はappendleft,コスト1の遷移はappendする
計算量O(N^2)定数倍重め、ダイクストラだとO(N^2*log(N))
"""
###################################################
N=INT()
sy,sx=MAP()
sy-=1;sx-=1
gy,gx=MAP()
gy-=1;gx-=1
#dist管理
dist=[[inf]*N for _ in range(N)]
dist[sy][sx]=0
#マップ読み込み
g=[list(input()) for _ in range(N)]
#移動方向に注意
dirc = [(1,1),(1,-1),(-1,1),(-1,-1)]
q=deque()
q.append((sy,sx))

#芝刈りBFS
while q:
    y,x=q.popleft()
    cost=dist[y][x]+1#始点のコスト+1
    for dx,dy in dirc:
        ny=y+dy
        nx=x+dx
        #costと比較して、コストが大きいマスはコストを更新してキューに追加(通常BFS)
        #コストが小さいマスはその先は見ない(そのマスを始点にすれば良いため)
        #障害物及び壁にあたってもその先は見ない
        while 0<=ny<N and 0<=nx<N and g[ny][nx]=='.' and dist[ny][nx]>=cost:
            if dist[ny][nx]==inf:
                q.append((ny,nx))
            dist[ny][nx]=cost
            ny+=dy
            nx+=dx


if dist[gy][gx]==inf:
    print(-1)
else:
    print(dist[gy][gx])