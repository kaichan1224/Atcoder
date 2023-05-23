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
1 2 2000
2 3 2004
3 4 1999
4 5 2001
3
1 2000
1 1999
3 1995

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・毎回bfsかdfsして、個数を数える方法だと部分点はとれる
・UnionFindは使いそうだけどよく思いつかない

<キーワード>
・クエリ先読み
・UnionFind

<ポイント>
・造られた年、つまり重みがある値wjより大きいもののみを通る
→大きい順に繋いで行ってその順にクエリを先読みして同時に処理し、ufで連結成分の個数を求める

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
    
N,M = MAP()
data = []
for _ in range(M):
    a,b,y = MAP()
    a,b = a-1,b-1
    #扱うデータがグラフの時、(造られた年、頂点a,b,_)
    data.append([y,a,b,0])
    
uf = UnionFind(N)
Q = INT()
for i in range(Q):
    #都市uに住んでてwより大きい都市で繋がっている数
    u,w = MAP()
    #(判定する年、判定用フラグ、連結成分を調べるのに必要な頂点,クエリのindex)
    data.append([w,N+1,u-1,i])
    
data.sort(reverse=True)
ans = [0]*Q

#年順に処理する
for y,a,b,i in data:
    if a==N+1:#クエリ
        ans[i] = uf.size(b)
    else:#グラフ
        uf.unite(a,b)
        
for a in ans:
    print(a)

    
    