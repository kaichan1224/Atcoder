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
6
8 3
4 9
12 19
18 1
13 5
7 6
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
<ポイント>
・クラスカル法：最小全域木を求める
(最小全域木：重み付き無向グラフからコストを最小化して作られた木)
・全ての辺を結ぶとO(N^2)でTLE
→隣り合うx,y座標同士で連結すればO(N)
・辺のコストでソートしてその辺のお互いの頂点がつながっていないならUnionFind
・最小全域木は辺の持ち方を工夫するタイプの問題が多いかも?
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
    
N = INT()
G = []
for i in range(N):
    x,y = MAP()
    G.append((i,x,y))
G.sort(key=lambda x:x[1])
ES = []
for i in range(N-1):
    ES.append((abs(G[i][1]-G[i+1][1]),G[i][0],G[i+1][0]))

G.sort(key=lambda x:x[2])
for i in range(N-1):
    ES.append((abs(G[i][2]-G[i+1][2]),G[i][0],G[i+1][0]))

#ES:(辺の重み,u,v)の順に辺を管理しておいて,コストが小さい順にソートして
#UnionFindすることを考える
def kruskal():
    ES.sort()    # 辺のコストが小さい順にソートする
    UFT = UnionFind(N)    # Union-Findの初期化
    res = 0
    for i in range(len(ES)):
        e = ES[i]
        if not UFT.is_same(e[1], e[2]):
            UFT.unite(e[1], e[2])
            res += e[0]
    return res
res = kruskal()
print(res)

