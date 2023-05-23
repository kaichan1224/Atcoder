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
#mod = 10**9+7
#mod = 998244353
######################################################
"""
橋：取り除いたときにグラフ全体が非連結になるような辺のこと

橋の本数→全ての辺について、それぞれの辺以外で連結したときに
グループの個数が複数（＝グラフ全体が非連結）ならばその辺は橋になる

＜アルゴリズム＞
1. 全ての辺 e1=(u1,v1) に対して以下を実行する
 * e1 以外の全ての辺 e2=(u2,v2) について以下を実行する
 * u2 と v2 を Union-Find Tree 上の同じ集合にまとめる (unite)
2. u1 と v1 が同じ集合になければ、e1 を除いたグラフは非連結で、e1 は橋
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
uf = UnionFind
N,M = MAP()
edge = [LIST() for _ in range(M)]
#取り除く辺番号
ans = 0
for v in range(M):
    uf = UnionFind(N)
    flag = False
    for e in range(M):
        if e!=v:
            uf.union(edge[e][0]-1,edge[e][1]-1)
    if uf.group_count()==1:
        flag = True
    if flag==False:
        ans += 1
print(ans)




