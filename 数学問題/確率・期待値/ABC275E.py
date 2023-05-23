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
10 5 6

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
dp[k][N]:k回目の時点でマスNにいる確率
dp[0][0] = 1
if n+m<=N:
    dp[k+1][N+M] += dp[k][N]*(1/M)
else:
    nxt = 2N-n-m
    dp[k+1][nxt] += dp[k][N]*(1/M)

dpで割る時modの計算に気をつけて!!!!!
遷移はどう考えても,足し算ですよね???
各独立の確率は足し算ですよ!

毎回division_modやるのはめちゃおそ!!!
→毎回同じ値なら、前計算しましょうや!
"""
#-------------------------------
def division_mod(a,b,mod):#a//b%modを正確に求める関数
    return a*pow(b,mod-2,mod)%mod
mod = 998244353
N,M,K = MAP()
dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1
ans = 0
Mmod = pow(M,mod-2,mod)
for k in range(K):
    for n in range(N):#今ますnにいる時の確率
        for m in range(1,M+1):
            if n+m<=N:
                dp[k+1][n+m] += dp[k][n]*Mmod
                dp[k+1][n+m] %= mod
            else:
                nxt = 2*N-n-m
                dp[k+1][nxt] += dp[k][n]*Mmod
                dp[k+1][nxt] %= mod
ans = 0
for k in range(K+1):
    ans += dp[k][N]
    ans %= mod
print(ans%mod)
            

        



