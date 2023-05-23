import io
import sys
sys.setrecursionlimit(10**7)
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
8
7 3 5 5 8 4 1 2
36 49 73 38 30 85 27 45



"""
sys.stdin = io.StringIO(_INPUT)
"""
<ポイント>
・向きが並ぶように並べたとき、逆向きが生じたらその部分が不満になる
・DAG→不満がない
*無向グラフの閉路→UnionFindでroot一致したら閉路
*有向グラフの閉路→トポロジカルソートができないとき閉路

・この問題のグラフは出次数=1→functional graph
→各頂点の出次数がちょうど1の単純な有向グラフのこと
→一つのサイクルから木が生えるという特徴がある
→連結成分ごとに、サイクル(閉路)は一つしかない
(連結成分:辺をいくつかたどって、たどり着ける関係にある頂点の集合)

・今回の問題では、不満が貯まるのはサイクルの部分のみ
・サイクル部分のうち一つだけ逆行する辺が生じる→サイクルの辺のうち、
最小のものを取り出せば良い。
・無向グラフでも今回は行ける（連結成分にサイクル一つの場合）
"""
#--------------------------------------------------------------
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
N = INT()
X = LIST()
X = [i-1 for i in X]
C = LIST()

uf = UnionFind(N)
ans = 0
for i in range(N):
    if not uf.same(i,X[i]):
        uf.union(i,X[i])
    else:
        now = i
        num = C[i]
        while True:
            now = X[now]
            num = min(num,C[now])
            if now==i:
                break
        ans += num
print(uf.all_group_members())
print(ans)






