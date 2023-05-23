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
4 2
1 3
2 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・いもす法でやる


<キーワード>
・一次元いもす法

<ポイント>
範囲ミスには注意

"""
#--------------------------------------------------------------
#N枚のIDカードとM個のゲート
N,M = MAP()
gate = [0]*(N+1)
LR = [LIST() for _ in range(M)]
for l,r in LR:
    l,r = l-1,r-1
    gate[l] += 1
    gate[r+1] -= 1
for i in range(N):
    gate[i+1] += gate[i]
ans = 0
for i in range(N+1):
    if gate[i]==M:
        ans += 1
print(ans)