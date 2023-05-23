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
"""
<考察>
逆からunionfindでいけそう?

<ポイント>
・今回の問題では、求めたいのは電気が通っている都市の数
→発電所の個数は関係ない、つまり、発電所は複数あるが発電所を一つとしてカウントできるのでは...
→N以降の頂点番号は、発電所をN一つにまとめることで、uf.size(N)で電気がつながっている
都市(+発電所一つ)の個数を知ることができる!!!!!!
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

N,M,E = MAP()
UV = []
for _ in range(E):
    u,v = MAP()
    u = min(u-1,N)
    v = min(v-1,N)
    UV.append((u,v))
Q = INT()
X = [INT() for _ in range(Q)]
uf = UnionFind(N+M)
ok = [True]*E
for x in X:
    ok[x-1] = False
for i in range(E):
    if ok[i]==True:
        uf.unite(UV[i][0],UV[i][1])

ans = []
for x in X[::-1]:
    ans.append(uf.size(N)-1)#Nが発電所なのでその分-1する
    uf.unite(UV[x-1][0],UV[x-1][1])
print(*ans[::-1],sep="\n")

    
    
    


