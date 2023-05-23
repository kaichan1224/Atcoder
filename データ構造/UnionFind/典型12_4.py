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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
5 5
42
2 3 4 3 4
2 3 2 3 2
1 4 1
2 4 1 2 2
1 1 2
1 4 5
1 3 3
2 4 2 1 3
1 3 5
2 2 4 2 3
2 2 4 2 5
2 3 4 5 1
2 3 1 2 2
2 3 1 1 2
2 2 4 5 2
2 3 2 5 3
1 4 3
2 3 3 3 5
2 3 1 3 2
1 1 5
2 4 4 5 3
1 1 4
2 1 3 2 5
2 4 3 1 4
2 2 3 3 3
1 2 1
1 2 5
2 1 4 5 3
2 4 4 2 5
2 4 2 2 4
1 2 2
2 4 1 5 2
1 2 4
2 3 1 4 1
1 4 4
2 3 2 2 1
2 1 1 5 2
1 4 2
2 4 2 3 5
1 3 2
1 3 4
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
グラフの連結はUnionFindでやると計算量減らせる
グリッド上の連結は移動方向に移動出来る点があったら、
二次元座標→一次元座標になおして元の点と移動後の点を連結すればよい
"""
######################################################
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    #要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    #要素xが属するグループと要素yが属するグループを結合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    #要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]
    #要素x,yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
    #要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    #すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    #グループの数を返す
    def group_count(self):
        return len(self.roots())
    #{ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
        
H,W = MAP()
Q = INT()
grid = [[False]*W for _ in range(H)]
uf = UnionFind(H*W)
for _ in range(Q):
    qu = LIST()
    if qu[0]==1:
        r,c = qu[1],qu[2]
        r,c = r-1,c-1
        grid[r][c] = True
        for dx,dy in dirc:
            nr,nc = r+dy,c+dx
            if not (0<=nr<H and 0<=nc<W):
                continue
            if grid[nr][nc]==True:
                uf.union(nr*W+nc,r*W+c)
    else:
        ra,ca,rb,cb =qu[1],qu[2],qu[3],qu[4]
        ra,ca,rb,cb = ra-1,ca-1,rb-1,cb-1
        if uf.same(ra*W+ca,rb*W+cb) and grid[ra][ca] and grid[rb][cb]:
            print('Yes')
        else:
            print('No')
        











