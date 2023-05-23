import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left
from typing import List 
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
4
0 0 2 0
3 0 0 0
0 0 0 4
0 1 0 0

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・1~100までの数字をk列k行目に配置したい
・行える操作は隣り合う行を交換、または隣り合う列を交換するの二つ
・最小何回の操作が必要か

・操作順序は問わない気がするので、愚直に最適解を求めるコードを書いてみる?
・いや全然だめ。というのも行を移動する時に他の数字も入れ替わってしまうため管理が難しい

<キーワード>
・X,Y独立に考える
・ソート順に並べ替える方法について(=転倒数)
・操作順序を問わない

<ポイント>
・問題のポイントを掴む
"""
#--------------------------------------------------------------
#転倒数を高速に求めることができる関数
def tentousu(A: List[int]):
    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0]*(n+1)
        def sum(self, i):
            # [0, i) の要素の総和を返す
            if not (0 <= i <= self.size): raise ValueError("error!")
            s = 0
            while i>0:
                s += self.tree[i]
                i -= i & -i
            return s
        def add(self, i, x):
            if not (0 <= i < self.size): raise ValueError("error!")
            i += 1
            while i <= self.size:
                self.tree[i] += x
                i += i & -i 
    bit = Bit(max(A)+1)
    ans = 0
    for i, a in enumerate(A):
        ans += i - bit.sum(a+1)
        bit.add(a, 1)
    return ans
    
N = INT()
grid = [LIST() for _ in range(N)]
Hlist = []
Wlist = []
for h in range(N):
    for w in range(N):
        if grid[h][w]>0:
            Hlist.append(grid[h][w])
for w in range(N):
    for h in range(N):
        if grid[h][w]>0:
            Wlist.append(grid[h][w])
print(tentousu(Hlist)+tentousu(Wlist))

