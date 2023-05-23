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
1
200000
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
実はグラフ問題に置き換える事ができるパターン
*A[i]!=A[N-i-1]ならば、A[i]とA[N-i-1]は同じ整数に置換しないといけない
*全ての組(i,j)について、頂点iとjが同じ連結成分に属していた場合、
iとjは最終的に同じ整数に置換されていないといけない
*ある一つの連結成分に含まれる整数を最小回数で全て同じするには、
一つの連結成分にk個含まれている場合、k-1回の操作が必要
*結論は、Aに含まれる整数の種類数-グラフの連結成分数の個数
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
A = LIST()
uf = UnionFind(max(A)+1)
for i in range(N//2):
    if A[i]!=A[N-i-1]:
        uf.unite(A[i],A[N-i-1])
cnt = 0
for i in uf.groups():
    cnt +=len(i)-1#同じグループに所属しているものは一つの整数に統一しないといけない
print(cnt) 
