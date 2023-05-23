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
tokyo
kyoto
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・dp[s][t]:Sがs文字目でTがt文字目の時の部分列の最大の長さ
・所謂、最長共通部分列ってやつ
ヒント
・もらうDPで考えた方楽。
<キーワード>
・LCS

<ポイント>
・s文字目とt文字目が同じ時は、dp[s][t] = dp[s-1][t-1]+1が成り立つ
"""
#--------------------------------------------------------------
S = input()
s = len(S)
T = input()
t = len(T)
dp = [[-INF]*(s+1) for _ in range(t+1)]
for sw in range(s+1):
    dp[0][sw] = 0
for th in range(t+1):
    dp[th][0] = 0
for sw in range(1,s+1):
    for th in range(1,t+1):
        if S[sw-1]==T[th-1]:
            dp[th][sw] = max(dp[th-1][sw-1]+1,dp[th-1][sw],dp[th][sw-1])
        else:
            dp[th][sw] = max(dp[th-1][sw],dp[th][sw-1])
print(dp[t][s])
        


