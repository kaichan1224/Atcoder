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
4 3 1
1 2
2 3
3 4
2 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・連結している数と見たらUnionFindを使いたくなる
・道路、鉄道それぞれUnionFindしてそれぞれのグループメンバーを集合の&とれば
一応答えを求めることができるが、各クエリでO(N)かかるので当然だめ。
・色々工夫しようとしたが思いつかず、diff見たらほぼ黄色やないかーーーい
(FIN)

<キーワード>
・unionfind + 連想配列
・iとjが鉄道・道路の両方で連結しているをどのようにunionfind等で実装すると 
計算量を改善することができるのか

<ポイント>
・意外とやろうとしていたことに近かった→じゃあやれよ定期
・同じグループか違うグループかはunionfindの根で判定することができる
i と j が鉄道・道路の両方で連結している ⇔ ar[i] = ar[j] ∧ br[i] = br[j] 
・set(uf.member(i)) & set(uf2.member(i))のlenを求めていたが、
dict[(uf.root(i),uf2.root(i))]の連想配列で同じペアがいくつ出てくるかを管理することで
解くことができる
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
    
N,K,L = MAP()
douro = UnionFind(N)
tetudou = UnionFind(N)
for _ in range(K):
    a,b = MAP()
    a,b = a-1,b-1
    douro.unite(a,b)
for _ in range(L):
    a,b = MAP()
    a,b = a-1,b-1
    tetudou.unite(a,b)
    
d = defaultdict(list)
for i in range(N):
    d[(douro.root(i),tetudou.root(i))].append(i)
ans = []
for i in range(N):
    print((len(d[(douro.root(i),tetudou.root(i))])),end=" ")




