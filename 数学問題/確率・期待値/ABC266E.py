import io
from re import T
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
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
ネットの記事参考にして解けた。
"""
#--------------------------------------------------------------
N = INT()
dp = [0]*(N+1)
dp[1] = 3.5
for i in range(1,N):
    t = int(dp[i])
    tmp = 0
    cnt = 0
    while t<6:
        cnt += 1
        t += 1
        tmp += t  
    dp[i+1] = (tmp/cnt)*(cnt/6)+((6-cnt)/6)*dp[i]
print(dp[N])
    