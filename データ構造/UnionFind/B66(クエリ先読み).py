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
3 2
1 2
2 3
4
2 2 3
1 2
2 1 3
1 1

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・クエリ先読みして、後ろから構築した方が楽かもしれない
・s,tパスが存在するかはUnionFindで確認すれば問題なし

<キーワード>
・UnionFind+クエリ先読み

<ポイント>
・辺の集合をsetで管理することで、点頂点に含まれているかをO(1)で判断できるようにした

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
uf = UnionFind(N)
AB = []
for _ in range(M):
    a,b = MAP()
    a,b = a-1,b-1
    AB.append([a,b])
Q = INT()
query = []#i番目のクエリを格納
mlist = []#運休になっていく順に、辺の番号を格納
for i in range(Q):
    q = LIST()
    if q[0]==1:
        x = q[1]
        mlist.append(x-1)
        query.append([x-1])
    else:
        u,v = q[1]-1,q[2]-1
        query.append([u,v])

mset = set(mlist)
for m in range(M):
    if m not in mset:#運休にしないものだったら
        uf.unite(AB[m][0],AB[m][1])

ans = []
#クエリ逆順に処理する
query.reverse()
for qu in query:
    if len(qu)==1:
        uf.unite(AB[qu[0]][0],AB[qu[0]][1])
    else:
        if uf.is_same(qu[0],qu[1]):
            ans.append("Yes")
        else:
            ans.append("No")
ans.reverse()
for a in ans:
    print(a)
        



        
    