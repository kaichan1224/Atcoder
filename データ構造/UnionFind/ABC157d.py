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
4 4 1
2 1
1 3
3 2
3 4
4 1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・a~b間の隣同士が友達関係で、abが友達関係にないかつブロック関係になかったら、
友達候補と言える。
・UnionFindを用いる

<ミスポイント1>
・1以上N以下の整数から成るある数列c0,c1,c2,⋯,cLが存在しc0=aであり、
cL=bでありi=0,1,⋯,L-1について人ciと人ci+1は友達関係にある。
→隣同士が友達は誤解釈、間接的に友達関係が正解。

<考察2>
・友達候補の個数
=友達グループの個数-ブロックしてる人の個数(友達かつ)-自分(1)-直接の友達の個数

<ミスポイント2>
・友達かつブロックしている人の個数をuf_block.size()-1で求めていた
→ブロックのブロック(←?)みたいな人もカウントしてしまっている!!!
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
    
N,M,K = MAP()
friend = UnionFind(N)
AB = [LIST() for _ in range(M)]#友達関係
CD = [LIST() for _ in range(K)]#ブロック関係
ans = [0]*N #各iについて、友達候補の数を答えてください

for a,b in AB:
    friend.unite(a-1,b-1)

block = [0]*N    
for c,d in CD:
    if friend.is_same(c-1,d-1):
        block[c-1] += 1
        block[d-1] += 1
    
direct_friend_num = [0]*N

for a,b in AB:
    direct_friend_num[a-1] += 1
    direct_friend_num[b-1] += 1

for i in range(N):
    ans[i] = friend.size(i)-1-block[i]-direct_friend_num[i]
print(*ans)
        
    

    
    

