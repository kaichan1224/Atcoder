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
from bisect import bisect_left,bisect_right
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
"""
二分探索を応用する問題
<ポイント>
求めたいのはxがある範囲の中で何個あるのか
→xの制約が10^5なので配列で管理することができる

*bisectはindexを返してくれる
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
d = defaultdict(list)
for i in range(N):
    d[A[i]].append(i)
Q = INT()
for _ in range(Q):
    l,r,x= MAP()
    l,r = l-1,r-1
    check = d[x]
    cnt = bisect_right(check,r)-bisect_left(check,l)
    print(cnt)
    