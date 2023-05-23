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
20
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・遷移を考えることができそうなものはDP!!!
・場合に分けに注意する!
・遷移はあっていても初期条件が間違っているとすべてが終わるので注意!
・場合分けのことも考慮すると初期設定はinfにすべき!
"""
#--------------------------------------------------------------
N = int(input())
A = LIST()
dp = [[INF]*(N+1) for i in range(2)]
#1番目を使わない場合
dp[1][1] = 0 
for i in range(1,N):
    #使う場合
    dp[0][i+1] = min(dp[0][i]+A[i],dp[1][i]+A[i])
    #使わない場合
    dp[1][i+1] = dp[0][i]
res = dp[0][N]

#1番目を使う場合
dp = [[INF]*(N+1) for i in range(2)]
dp[0][1] = A[0]
for i in range(1,N):
    #使う場合
    dp[0][i+1] = min(dp[0][i]+A[i],dp[1][i]+A[i])
    #使わない場合
    dp[1][i+1] = dp[0][i]
res2 = min(dp[0][N],dp[1][N])
print(min(res,res2))







