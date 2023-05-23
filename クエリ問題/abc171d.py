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
2
1 2
3
1 100
2 100
100 1000
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・差分更新をうまくやる
・バケットをうまく使う
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
d = defaultdict(int)
Asum = sum(A)
for a in A:
    d[a] += 1
Q = INT()
for _ in range(Q):
    b,c = MAP()
    Asum -= b*d[b]
    Asum += c*d[b]
    d[c] += d[b]
    d[b] = 0
    print(Asum)
