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
mod = 998244353
#--------------------------------------------------------------
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・ai<=ci<=biかつ広義単調増加である数列CNとしてあり得る数列の個数は
→制約的に2次元DP
dp[i][c]:値がcかつ配列の長さがi番目の時点であり得る数列の個数
dp[i][c] += dp[i-1][cよりも小さい値かつ、Ai-1<=x<=Bi-1の値]
・とりあえず実装はできたが、制約オーバー
・累積和等をうまく使って計算量を改善できないか考える
→うまくできたと思ったら2WA:(
・結論は、N=3000(ai,biが3000の時)のケースでWAが出ていた
→今度からDP配列はギリギリじゃなくて大きめにとる!!!!!(30分溶かした)
    
<キーワード>
・2次元DP
・累積和で処理高速化

<ポイント>
・DP配列は大きめにとる!!
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
B = LIST()
dp = [[0]*(3005) for _ in range(N+1)]
for c in range(A[0],B[0]+1):
    dp[1][c] = 1

#累積和をとる
for c in range(A[0]+1,B[0]+1):
    dp[1][c] += dp[1][c-1]
    
def debug():
    for c in range(1,N+1):
        for i in range(4):
            print(dp[c][i],end=" ")
        print()
    
for i in range(2,N+1):
    for c in range(A[i-1],B[i-1]+1):
        if c>=B[i-2]:
            dp[i][c] += dp[i-1][B[i-2]]-dp[i-1][A[i-2]-1]
        elif A[i-2]<=c<B[i-2]:
            dp[i][c] += dp[i-1][c]-dp[i-1][A[i-2]-1]
        """
        要改善:オーダーO(N^3)の答え
        for x in range(A[i-2],B[i-2]+1):
            if c>=x:
                dp[i][c] += dp[i-1][x]
        """
    for c in range(A[i-1]+1,B[i-1]+1):
        dp[i][c] += dp[i][c-1]%mod
print((dp[N][B[N-1]])%mod)
    
        
