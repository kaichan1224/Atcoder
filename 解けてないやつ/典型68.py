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
4
7
0 1 2 3
1 1 2 1
1 3 4 5
0 3 4 6
1 3 4 5
0 2 3 6
1 3 1 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・Ayの値が確定している→AxからAyまでの隣り合った関係がすべてわかっている

<ポイント>
・クエリ先読み

・重み付きUnionfind:普通のunionfindに加えて各ノード間の距離も管理する
merge(x,y,w):weight(y)+weight(x)+wとなるようにマージ
issame(x,y):xとyが同じグループにいるかどうかを判断する
diff(x,y):xとyが同じグループにいるとき、weight(y)-weight(x)を返す


"""
#--------------------------------------------------------------
# 偶奇で重みをy - x = v か y - x = -v かで変えて重み付きUnionFindでクエリに答える．
# People on a Line に似ている．

class WeightedUnionFind:
    __slots__ = ("root", "diff_weight")

    def __init__(self, N):
        """root[v] = vの親, diff_weight[v] = 根からの重み"""
        N += 1
        self.root = [-1] * N
        self.diff_weight = [0] * N

    def find(self, x):
        que = []
        while self.root[x] >= 0:
            que.append(x)
            x = self.root[x]

        for i in reversed(que):
            self.diff_weight[i] += self.diff_weight[self.root[i]]
            self.root[i] = x

        return x

    def weight(self, x):
        self.find(x)
        return self.diff_weight[x]

    def difference(self, x, y):
        """weight(y) - weight(x)"""
        return self.weight(y) - self.weight(x)

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y, w):
        """weight(y) - weight(x) = w となるように union する"""
        x_root = self.find(x)
        y_root = self.find(y)
        w += self.diff_weight[x]
        w -= self.diff_weight[y]
        x, y = x_root, y_root
        if x == y:
            return
        if self.root[y] < self.root[x]:
            x, y, w = y, x, -w
        self.root[x] += self.root[y]
        self.root[y] = x
        self.diff_weight[y] = w

n = INT()
Q = INT()
res = []
uf = WeightedUnionFind(n)
for _ in range(Q):
    t, x, y, v = map(int, input().split())
    x -= 1 
    y -= 1
    if t==1:
        if uf.same(x, y):
            k = uf.difference(y, x)
            if x % 2 == 0:
                k -= v
            else:
                k += v
            if y % 2 == 0:
                k = -k
            res.append(str(k))
        else:
            res.append("Ambiguous")
    else:
        if x % 2 == 0:
            uf.union(y, x, v)
        else:
            uf.union(y, x, -v)

print("\n".join(res))




