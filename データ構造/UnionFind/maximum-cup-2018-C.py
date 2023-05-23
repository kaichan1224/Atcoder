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
4
2
3
4
1

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
天使→悪魔
悪魔→天使
悪魔が最大何人
悪魔が最大で何人のときに矛盾が起きないかを二部探索すればいけそう?
→判定部分をどうやってやるかが重要
→上から順番に決めつけて行って、途中で矛盾が生じたらFalse、そうでなければTrue
→上から決めつけるのではなく、グラフ上で順に探索した方が良さそう
->グラフの連結成分ごとにみる??
探索するたびに、悪魔、天使が交互に入れ替わるので矛盾を調べることができる(?)

<ポイント>
・条件をちゃんと読む！
・問題になっているグラフは、N頂点N辺でありかつ、出自数は1,Ai!=Ajであるから
必ず全てがサイクルの有向グラフとして考えられるが、連結成分ごとに別々に考える必要があるかもしれない
・各連結のグラフについて、連結成分の個数が奇数の場合は、成り立たないことがわかるのでufで解ける!!
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
A = [INT() for _ in range(N)]
uf = UnionFind(N)
for i in range(N):
    uf.unite(i,A[i]-1)
groups = uf.groups()
ans = 0
for a in groups:
    if len(a)%2==1:
        print(-1)
        exit()
    else:
        ans += len(a)//2
print(ans)




