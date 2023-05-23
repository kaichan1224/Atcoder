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
3
1 2 10
2 3 20

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<主客転倒>
得点Aiをいくつか足した和で表される総得点Siが沢山あって、ありうる全ての場合について 
Siを足し合わせたいときに、 Aiが何回足されるかを考えるテク
→ゲームごとの得点の総和をAiが足された回数に話をすり替える
→「和の形の数え上げをみたら、和の形のコストのまとめ方を変える」

<ポイント>
重み付き木
u→vの最短パスに含まれる辺の重みの最大値の総和
u:頂点1～N-1,v:u+1～N
O(NlogN)が限界

<思考の流れ>
全ての頂点間の組み合わせについてf(i,j)→O(N^2)
↓
全てのf(i,j)について、f(i,j)*それを満たす頂点間の組み合わせ
↓(組み合わせの部分を高速で求めたい)
f(i,j)がとある辺kの重みw[k]である場合について考えると
これは単純に通る頂点の組はu[k]側の頂点の個数＊v[k]側の頂点の個数
↓しかしこれでは別のw[k]以上の頂点が含まれる可能性がある
u[k]側のw[k]以下の辺を使って到達可能な頂点の個数×v[k]側のw[k]以下の辺を使って到達可能な頂点の個数
↓
UnionFindを使ってうまく処理できそう
具体的にはw[k]辺を処理する場合にw[k]以下の辺について結合されている必要があるので
辺の評価は重みが小さいものから順番に行う
"""
#--------------------------------------------------------------
class UnionFind:
    from typing import List

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def unite(self, x, y) -> int:
        """
        xとyを併合
        """
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return 0

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return self.parent[x]

    def is_same(self, x, y) -> bool:
        """
        xとyが同じ連結成分か判定
        """
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        """
        xの根を取得
        """
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        """
        xが属する連結成分のサイズを取得
        """
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """
        全連結成分のサイズのリストを取得
        計算量: O(N)
        """
        sizes = []

        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """
        全連結成分のサイズの内容のリストを取得
        計算量: O(N・α(N))
        """
        groups = dict()

        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)

        return list(groups.values())
N = INT()
G = [[]for _ in range(N)]
point = []
for _ in range(N-1):
    u,v,w = MAP()
    point.append([u-1,v-1,w])
point.sort(key=lambda x:x[2])
ans = 0
uf = UnionFind(N)
for u,v,w in point:
    ans += w*uf.size(u)*uf.size(v)
    uf.unite(u,v)
print(ans)








