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
4 10
4 2 3 2

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
Nがクソ小さい
2頂点の組み合わせがN*(N-1)/2なのでグラフを作ることができる

<ポイント>
・x,y間のコストを加算し片方をできなくなるまで消す
->最大全域木を構成するのと同じ意味
・ペアにして片方だけ消していくのは、木になる

・繰り返し2乗法
"""
#-------------------------------
N,M = MAP()
A = LIST()
ES = []
for i in range(N):
    for j in range(i+1,N):
        cost = pow(A[i],A[j],M)+pow(A[j],A[i],M)
        cost %= M
        ES.append((cost,i,j))
        ES.append((cost,j,i))

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

#ES:(辺の重み,u,v)の順に辺を管理しておいて,コストが小さい順にソートして
#UnionFindすることを考える
def kruskal():
    ES.sort(reverse=True)    # 辺のコストが小さい順にソートする
    UFT = UnionFind(N)    # Union-Findの初期化
    res = 0
    for i in range(len(ES)):
        e = ES[i]
        if not UFT.is_same(e[1], e[2]):
            UFT.unite(e[1], e[2])
            res += e[0]
    return res

ans = kruskal()
print(ans)
    



