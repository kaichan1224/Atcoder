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
mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
140
aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
状態DP
現在の状態（定数個の場合も多い）を意識してもつDPで解ける問題は多い
DPは通り数が大きくなる傾向があるので、%mod忘れないように注意
"""
######################################################
N =INT()
S =input()
alp = 'atcoder'
dp = [[0]*(N+1) for _ in range(8)]
for i in range(N+1):
    dp[0][i] = 1
for i in range(N):
    for j in range(7):
        if S[i]==alp[j]:
            dp[j+1][i+1] += dp[j][i]
        dp[j+1][i+1] += dp[j+1][i]
        dp[j+1][i+1] %= mod
print(dp[7][N]%mod)



