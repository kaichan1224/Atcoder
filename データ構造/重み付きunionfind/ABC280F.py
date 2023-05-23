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

<別解>
・重み付きunionfind:非ゼロ閉路対応verを用いる
・そうでなくても、行ける
"""
#-------------------------------
class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)
        self.loop = set()
 
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y
 
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx==ry and w - self.weight[x] + self.weight[y] != 0:
            self.loop.add(rx)
            return
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
            if rx in self.loop:
                self.loop.discard(rx)
                self.loop.add(ry)
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
            if ry in self.loop:
                self.loop.discard(ry)
                self.loop.add(rx)
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def diff(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx!=ry:
            return "nan"
        if rx in self.loop:
            return "inf"
        return self.weight[x] - self.weight[y]

N,M,Q = MAP()
uf = WeightedUnionFind(N)
G = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    uf.union(a,b,c)
for _ in range(Q):
    x,y = MAP()
    x,y = x-1,y-1
    print(uf.diff(x,y))




