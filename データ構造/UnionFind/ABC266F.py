import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
#-------------------------------
"""
・連結な単純無向グラフ
・N頂点N辺=木+１辺
a->bの間に頂点数が3のものがあればNo,そうでなければYes
->これ違います

・a->b間に閉路があればNo,そうでなければYes
→どうやって実装するのというお話

・なもりグラフ
N頂点N辺の連結なグラフ
ちょうど一つの閉路及び、その閉路上の頂点を根とする木としてみることができる
閉路(○)に木が生えている状態がイメージしやすい

・a->b間に閉路があるかを判定する方法
実装方法は色々あるが、
出自数が1のものから順番に切って行って、残ったやつが閉路になる
その際に、切ったものはグループにする
"""
#-------------------------------

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

N = INT()
G = [[] for _ in range(N)]
uf = UnionFind(N)
outNum = [0]*N
for _ in range(N):
    u,v = MAP()
    u,v = u-1,v-1
    G[u].append(v)
    G[v].append(u)
    outNum[u] += 1
    outNum[v] += 1
#出自数が1の頂点から順番に処理する
que = deque()
for i in range(N):
    if outNum[i]==1:
        que.append(i)
while que:
    now = que.popleft()#出自数が1の点
    nxt = G[now][0]#nowにつながっている点,出自数は1なので隣接リストにつながっている点の数も当然一つ
    outNum[now] -= 1
    outNum[nxt] -= 1
    G[nxt].remove(now)#つながっている点から今見ている点を消す
    uf.unite(now,nxt)
    if outNum[nxt]==1:
        que.append(nxt)

#クエリ処理
Q = INT()
for _ in range(Q):
    x,y = MAP()
    x,y = x-1,y-1
    if uf.is_same(x,y):
        print("Yes")
    else:
        print("No")



