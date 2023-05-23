class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)
        self.loop = set()
 
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y
 
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx==ry and w - self.weight[x] + self.weight[y] != 0:
            self.loop.add(rx)
            return
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
            if rx in self.loop:
                self.loop.discard(rx)
                self.loop.add(ry)
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
            if ry in self.loop:
                self.loop.discard(ry)
                self.loop.add(rx)
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def diff(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx!=ry:
            return "nan"
        if rx in self.loop:
            return "inf"
        return self.weight[x] - self.weight[y]

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
3 3
1 2 1
2 3 1
1 3 2


"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------
"""
新たに接続する時に、既に閉路が存在しており、かつ距離が異なるときはNG

"""
#-------------------------
N,M = MAP()
uf = WeightedUnionFind(N)
for _ in range(M):
    l,r,d = MAP()
    l,r = l-1,r-1
    if (not uf.same(l,r)):
        uf.union(l,r,d)
    else:
        if uf.diff(l,r) != d:  
            print("No")
            exit()
print("Yes")

