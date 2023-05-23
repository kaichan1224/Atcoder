import io
import sys
sys.setrecursionlimit(10**7)
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
6 2
10 10 10 9 8 8
1 4
2 1
2 5
3 2
6 4
1 4
2 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・N頂点の根付き木
・根付き木を根から子の方向へたどり、各頂点ごとに部分木に含まれる頂点に書かれた整数をメモる?
→高々大きい1~20番目のものを出力すれば良いので、順番に追加していって、
20番以下になったらそれと比較して小さい方を削除を行えば良い。
-具体的には普通の配列に要素を追加して要素数が20を超えたら最小値と比較して削除、追加を行う
-出力する時にソートしてKi番目を出力すれば良い
・このようにすることで、高々1回dfsすれば良いことがわかる。
↓
そんなことしなくても、要素数が20までの範囲でソートして値を保てば良い

<キーワード>
・木:平路を持たないような連結なグラフ
-グラフの点の数がNの時辺の数はN-1
-隣接していない任意の２点を加えると閉路が一つだけできる
-グラフの辺を一本でも消すと連結ではなくなる

・森:閉路を持たないようなグラフのこと
-イメージは木の集まり(なお木単体も森である)

・根付き木って何?
-木に対して、特定の1つの頂点を特別扱いして根とよび、根をもつ木のことを根付き木と呼ぶ。
-根をもたない木に対して、そのことを強調するときは根なし木と呼ぶ。

・部分木って何?
-根付き木のある頂点viを根とする部分木はvを根とした木
-頂点viも当然その中に含まれるのに注意!(逆になぜ含まれないと思っていたか謎)

<ポイント>
・dfsとbfsの用途をちゃんと使い分ける!!!
・再掲
グラフ問題のアプローチ
DFS,BFS,etc:更新の仕方   DP:状態の持ち方

BFS:最小手が関係するとき
DFS:それ以外(根からの距離、頂点にたどり着けるか判定、連結成分個数
    二部グラフ判定、閉路検出、他にもたくさん)
    
・部分木→dfsで扱うことがほとんど
・オイラーツアーって何?
-根付きを根からDFSし根に戻ってくる行きと戻りの経路を1次元のテーブルに記録したもの

・dfsのタイミングについて(再掲)
def dfs(v,pre):
    #頂点が初めて探索されるタイミング(行きがけ)(上から下に行くタイミング)
    ans.append(v+1)
    for u in G[v]:
        if u!=pre:
            dfs(u,v)
            #子の一つが探索終わったタイミング
            ans.append(v+1)
    #頂点が探索終えたタイミング(帰りがけ) (下から上に行くタイミング)

・ミス
-dfs(nxt,now)をdfs(nxt,pre)としてしまっていた  

・間違い
-子の一つが探索終わったタイミングで、今まで通った点のリストをextendする  
(X[nxt]を追加してしまっていた)
"""
#--------------------------------------------------------------
N,Q = MAP()
X = LIST()
G = [[] for _ in range(N)]
vlist = [[] for i in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
    
def dfs(now,pre):
    #頂点が初めて探索されるタイミング
    vlist[now].append(X[now])
    for nxt in G[now]:
        if nxt!=pre:
            dfs(nxt,now)
            vlist[now].extend(vlist[nxt])
            vlist[now].sort(reverse=True)
            vlist[now] = vlist[now][:20]
    
dfs(0,-1)
for _ in range(Q):
    v,k = MAP()
    v,k = v-1,k-1
    print(vlist[v][k])
    