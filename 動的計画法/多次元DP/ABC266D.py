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
dp[t][i]:i番目をt秒に取った時の大きさの合計の最大値

"""
#--------------------------------------------------------------
N = INT()
TXA = [LIST() for _ in range(N)]
dp = [[0]*5 for _ in range(TXA[N-1][0]+1)]
sunuke = [[0]*5 for _ in range(TXA[N-1][0]+1)]
for t,x,a in TXA:
    sunuke[t][x] = max(sunuke[t][x],a)
for t in range(1,TXA[N-1][0]+1):
    for i in range(5):
        if t==1 and i==2:
            break
        if t==2 and i==3:
            break
        if t==3 and i==4:
            break
        if i==0:
            dp[t][i] = max(dp[t-1][i],dp[t-1][i+1]) + sunuke[t][i]            
        elif i==4:
            dp[t][i] = max(dp[t-1][i],dp[t-1][i-1]) + sunuke[t][i]
        else:
            dp[t][i] = max(dp[t-1][i],dp[t-1][i-1],dp[t-1][i+1]) + sunuke[t][i]
ans = 0
for i in range(5):
    ans = max(ans,dp[TXA[N-1][0]][i])
print(ans)
    
            
        
    
    


