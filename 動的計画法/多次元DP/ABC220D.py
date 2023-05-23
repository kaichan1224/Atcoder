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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
mod = 998244353
######################################################
_INPUT = """\
5
0 1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
配るDP
modが出でくる数え上げはだいたいDP説
遷移、用意するDP配列をきちんと考えてとく
試行錯誤必要！
"""
######################################################
N = INT()
A = LIST()
q = deque()
q.extend(A)
dp = [[0]*(N) for _ in range(10)]
dp[A[0]][0] = 1
for i in range(N-1):
    for j in range(10):
        if dp[j][i]>0:
            dp[(j*A[i+1])%10][i+1]+=dp[j][i]
            dp[(j+A[i+1])%10][i+1]+=dp[j][i]
            dp[(j*A[i+1])%10][i+1]%=mod
            dp[(j+A[i+1])%10][i+1]%=mod
#print(dp)
for i in range(10):
    print(dp[i][N-1]%mod)
        
    



