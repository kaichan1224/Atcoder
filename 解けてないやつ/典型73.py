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
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
22
b a b b a b b b a b a a a a b b a b b a a a
1 7
4 14
12 22
2 4
21 17
3 20
7 8
20 14
15 11
8 14
9 12
17 8
6 20
11 20
18 19
10 8
22 20
13 21
5 14
19 20
16 14

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・辺の削除→Unionfindで逆から考える?
・辺の削除の仕方
・すべての辺のつなぎ方-(Aだけを繋ぐ方法)-(Bだけを繋ぐ方法)
・繋ぐ方法は木DP?
"""
#-------------------------------------------------------------- 
N = INT()
c = list(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

dp = [0]*N
dpa = [0]*N
dpb = [0]*N

def dfs(v,pre):
    for u in G[v]:
        if u!=pre:
            dfs(u,v)
            dp[]

dfs(0,-1)



