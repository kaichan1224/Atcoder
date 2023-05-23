import io
import sys
#sys.setrecursionlimit(10**7)
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
5 6 2
1 2 5
1 3 3
2 3 4
2 5 7
3 4 6
4 5 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・K個の都市で大会を開催しなければならない
・K=1の時、最小全域木が答えになる

・Kが複数の時、いずれかの集めればいい時もある
→K-1の回数分、最小全域木から辺を分割(=切る)ことができる
→今度はコストが大きい順にK-1回全域木に含まれるものを切っていけば良い

<キーワード>
・最小全域木の問題

<ポイント>
AC
MLEになったけどpypy->pythonで解決
"""
#--------------------------------------------------------------
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
        """全連結成分のサイズのリストを取得 O(N)"""
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
N,M,K = MAP()
ES = []
for _ in range(M):
    a,b,c = MAP()
    ES.append((c,a-1,b-1))

uf = UnionFind(N)
ES.sort()
s = set()
idx = 0
ans = 0
for cost,a,b in ES:
    if not uf.is_same(a,b):
        uf.unite(a,b)
        ans += cost
        s.add(idx)
    idx += 1

if K==1:
    print(ans)
else:
    now = N-1
    cutcnt = 0#切った回数(K-1回切ったら終了)
    for i in range(M)[::-1]:
        if i in s:
            ans -= ES[i][0]
            cutcnt += 1
        if cutcnt==K-1:
            break
    print(ans)
        


