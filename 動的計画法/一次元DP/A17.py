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
"""
<考察>

<キーワード>
・DP復元について

<ポイント>
・DPは1indexにしましょう。
・DPの復元はゴールから逆向きに。
"""
#--------------------------------------------------------------
N = INT()
A = [0]+[0]+LIST()
B = [0]+[0]+[0]+LIST()
dp = [INF]*(N+2)
dp[1] = 0
dp[2] = A[2]
for i in range(3,N+1):
    dp[i] = min(dp[i],dp[i-1]+A[i],dp[i-2]+B[i])
now = N
ans = [N]
while now!=1:
    if dp[now-1]+A[now] ==dp[now]:
        now -= 1
        ans.append(now)
    elif dp[now-2]+B[now] == dp[now]:
        now -= 2
        ans.append(now)
ans.reverse()
print(len(ans))
print(*ans)
        
