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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
2 3
1 2 -1
1 2 2
1 1 3
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
自分の思考
*unionfindで連結判定?
*辺も取り除いた後もグラフが連結→最小全域木?
→あってた

より正確に考える
削除する辺のスコアの最大化→辺を元にもどす(全域木をつくる)ときに
報酬がすくなるなるようにする
ただし、C<0の辺のは削除しない←色々実験してみて考える!

<クラスカル法のアルゴリズム>
全ての辺集合Eをコストが小さい順にソート
for 辺 in E:
    if 構築済みの辺集合に新たに加えても閉路を作らない:
        グラフを結合(unite)
return 全域木の辺のコストの和(最小)
"""
######################################################
from typing import List
class UnionFind:
    """0-indexed"""
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n  # 辺がないとき、連結成分はn個あります

    def unite(self, x, y):
        """xとyをマージ"""
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return 0
        self.__group_count -= 1  # 木と木が合体するので、連結成分数が1減ります
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return self.parent[x]

    def is_same(self, x, y):
        """xとyが同じ連結成分か判定"""
        return self.root(x) == self.root(y)

    def root(self, x):
        """xの根を取得"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x):
        """xが属する連結成分のサイズを取得"""
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """全連結成分のサイズのリストを取得 O(N)
        """
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """全連結成分の内容のリストを取得 O(N・α(N))"""
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())

    def group_count(self) -> int:
        """連結成分の数を取得 O(1)"""
        return self.__group_count  

#UnionFindクラスを利用する
V, E = MAP()    # Vは頂点数、Eは辺数
es = []
tmp = 0
for _ in range(E):
    s, t, c = MAP()
    tmp += c
    if c<0:
        c = 0
    es.append([c, s-1, t-1])    # c(辺のコスト)でソートできるように最初の要素にしておく

def kruskal():
    es.sort()    # 辺のコストが小さい順にソートする
    UFT = UnionFind(V)    # Union-Findの初期化
    res = 0
    for i in range(E):
        e = es[i]
        if not UFT.is_same(e[1], e[2]):
            UFT.unite(e[1], e[2])
            res += e[0]
    return res

res = kruskal()
print(tmp-res)


