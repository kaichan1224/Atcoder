import io
import sys
sys.setrecursionlimit(10**9)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
5
1 2
1 3
1 4
4 5
3
2 3
2 5
2 4
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
* LCAは構築にNlogN,クエリ処理にlogNなので、任意の2頂点間距離などを
求めるクエリ問題で有効
* 無向グラフならよい
* lcaを使うときは辺の重みを必ず書いておく(重みなし無向グラフの場合は1)
また以下の3つの処理が可能
1.任意の2頂点間距離
2.任意の2頂点を結ぶパス上の最小コスト辺、最大コスト辺
3.任意の2頂点を含む部分木の要素数
"""
######################################################
#LCA(ダブリング)のクラスを拝借
class LcaDoubling:
    """
    links[v] = { (u, w), (u, w), ... }  (u:隣接頂点, w:辺の重み)
    というグラフ情報から、ダブリングによるLCAを構築。
    任意の2頂点のLCAおよび距離を取得できるようにする
    """
    def __init__(self, n, links, root=0):
        self.depths = [-1] * n
        self.distances = [-1] * n
        prev_ancestors = self._init_dfs(n, links, root)
        self.ancestors = [prev_ancestors]
        max_depth = max(self.depths)
        d = 1
        while d < max_depth:
            next_ancestors = [prev_ancestors[p] for p in prev_ancestors]
            self.ancestors.append(next_ancestors)
            d <<= 1
            prev_ancestors = next_ancestors

    def _init_dfs(self, n, links, root):
        q = [(root, -1, 0, 0)]
        direct_ancestors = [-1] * (n + 1)  # 頂点数より1個長くし、存在しないことを-1で表す。末尾(-1)要素は常に-1
        while q:
            v, p, dep, dist = q.pop()
            direct_ancestors[v] = p
            self.depths[v] = dep
            self.distances[v] = dist
            q.extend((u, v, dep + 1, dist + w) for u, w in links[v] if u != p)
        return direct_ancestors

    def get_lca(self, u, v):
        du, dv = self.depths[u], self.depths[v]
        if du > dv:
            u, v = v, u
            du, dv = dv, du
        tu = u
        tv = self.upstream(v, dv - du)
        if u == tv:
            return u
        for k in range(du.bit_length() - 1, -1, -1):
            mu = self.ancestors[k][tu]
            mv = self.ancestors[k][tv]
            if mu != mv:
                tu = mu
                tv = mv
        lca = self.ancestors[0][tu]
        assert lca == self.ancestors[0][tv]
        return lca

    def get_distance(self, u, v):
        lca = self.get_lca(u, v)
        return self.distances[u] + self.distances[v] - 2 * self.distances[lca]

    def upstream(self, v, k):
        i = 0
        while k:
            if k & 1:
                v = self.ancestors[i][v]
            k >>= 1
            i += 1
        return v

N = INT()
G = [[] for _ in range(N)]
for _ in range(N-1):
    x,y = MAP()
    x,y = x-1,y-1
    G[x].append((y,1))
    G[y].append((x,1))
lca = LcaDoubling(N,G)
Q = INT()
for _ in range(Q):
    a,b = MAP()
    a,b = a-1,b-1
    print(lca.get_distance(a,b)+1)
