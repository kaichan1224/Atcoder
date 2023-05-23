import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate

#from pyrsistent import T
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
8 7
7 8
3 4
5 6
5 7
5 8
6 7
6 8
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
UnionFindは辺の削除ができないので「逆から処理」のパターン
後ろから見るときに一旦グラフの隣接リストを作ってから見ると楽

<ポイント>
グラフの連結成分数は、初期値はすべてつながっていない状態
=>Nであることに注意!!!
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
        return self.__group_count  # 変数を返すだけなので、O(1)です

N,M = MAP()
AB = []
G = [[] for _ in range(N)] #これつくってから後ろから見る方が圧倒的に楽なのになぜしない
for _ in range(M):
    a,b = MAP()
    G[a-1].append(b-1)
uf = UnionFind(N)

ans = [0]*N
for u in range(N)[::-1]:
    #ここが一番の重要ポイント
    ans[u] = uf.group_count()-(u+1)
    for v in G[u]:
        uf.unite(u,v)

for x in ans:
    print(x)
    






