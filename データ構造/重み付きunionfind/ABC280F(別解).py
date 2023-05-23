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
5 5 3
1 2 1
1 2 2
3 4 1
4 5 1
3 5 2
5 3
1 2
3 1

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<問題のポイント>
・a->bが繋がってなければnan
・木構造の時はそのまま求めるだけ.
->今回の問題では同じ道を往復すると、ポイントは0になる
->各頂点のポテンシャルを一回bfs等で求めた後、差分を取れば良い
・infになる場合について
->途中の経路でサイクルがあり、かつ、サイクル内での重みが0でない場合
(向きを変えれば必ず+になりうる)

<重み付きunionfindについて>
・merge(x,y,w):weight[y]=weight[x]+wとなるように結合
・diff(x,y):weight[y]-weight[x]
・same(x,y):同じグループか判定(結合判定や閉路判定で使用)
・辺に重みをつけて、ポテンシャルでコストを求める感じっぽい

<別解>
・重み付きunionfind:非ゼロ閉路対応verを用いる
・そうでなくても、行ける
・重みが0でない閉路を検出した際は、その連結成分を架空の頂点N+1に接続しておくと楽
"""
#-------------------------------
class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)
    
    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y
    
    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
    
    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

N,M,Q = MAP()
uf = WeightedUnionFind(N+1)
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    if uf.same(a,b) and uf.diff(a,b) != c:
        uf.union(a,N,0)
    uf.union(a,b,c)
for _ in range(Q):
    x,y = MAP()
    x,y = x-1,y-1
    if uf.same(x,y):#xとyが繋がっているか
        if uf.same(x,N):#0でない閉路が存在するか
            print("inf")
        else:
            print(uf.diff(x,y))
    else:
        print("nan")




