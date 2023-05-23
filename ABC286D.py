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
2 19
2 3
5 6

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
INF = float("inf")
n, m = MAP()

dp = [False for i in range(m + 1)]
dp[0] = True

for i in range(n):
    ai, bi = MAP()
    dp1 = [0 if dp[i] else INF for i in range(m + 1)]
    for j in range(m - ai + 1):
        if dp[j] and not dp[j + ai] and dp1[j] < bi:
            dp[j + ai] = True
            dp1[j + ai] = dp1[j] + 1

if dp[m]:
    print("Yes")
else:
    print("No")


