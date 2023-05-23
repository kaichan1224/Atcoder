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
5 4
2 2 2 2 2
1 1 2
1 1 3
1 2 3
2 2 2


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・dict[(uf.root(i),uf2.root(i))]の連想配列で同じペアがいくつ出てくるかを管理する
パターンのやつ?

・考え方としては似ているが少し異なる

・xに合流している生徒のうち、クラスyに属している生徒の数

<キーワード>
・UnionFind + dplikeな問題
・マージテク:データ構造を併合していく時、併合の仕方を工夫することで計算量を小さく抑えるテクニック
・連想配列　in リスト　の多次元データ構造で管理

<ポイント>
・今回では、d[a][c]:aが所属しているグループにクラスcの人は何人いるか?のデータを管理すれば良い
・dp[uf.root(a)][c]:cは全てのクラスを管理する必要はなく、生徒bのいるクラスのみを動かせば良いので、
連想配列で管理すれば良い。

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
N,Q = MAP()
C = LIST()
uf = UnionFind(N)
 #辞書d(生徒グループのリーダー、クラス名)がn人いる
D = []
for i in range(N):
    d = defaultdict(int)
    d[C[i]] = 1
    D.append(d)
for _ in range(Q):
    query = LIST()
    if query[0]==1:
        a,b = query[1],query[2]
        a,b = a-1,b-1
        if not uf.is_same(a,b):
            #a,bそれぞれのグループのリーダーについて、グループが小さい方から大きい方にグループを統合して考える
            a = uf.root(a)
            b = uf.root(b)
            #サイズが大きい法をa
            if uf.size(a) < uf.size(b):
                a,b = b,a
            #クラスが大きい方からクラスが小さい方へ移す
            for classname,num in D[b].items():
                D[a][classname] += num
            uf.unite(a,b)
    else:
        x,y = query[1],query[2]
        x -= 1
        print(D[uf.root(x)][y])