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
6
2 4 4 9 4 9
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
全探索、計算量改善
1sec→10^8でギリギリ
2sec→2*10^8
今回はN=10^4だからO(N^2)で間に合う!しかも定数倍は1/2なので余裕
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
#愚直
ans = 0
for l in range(N):
    num = A[l]
    for r in range(l,N):
        num = min(num,A[r])#選べる区間の中で最小のもの*個数分選べる
        ans = max(ans,num*(r-l+1))
print(ans)


