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
mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
1

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
全ての項が3以上で総和がSとなる数列がいくつあるか
*dpっぽいというのはあっていた
*遷移をもっと効率のよいものがあった(二次元DPで考えてしまった)
*A[n]:S=nのときの個数とすると,A[n]=A[n-1]+A[n-3]←3以上の整数
*A[0]=1としておくと遷移がきちんと成り立つ

注:dpの長さが短いとき,初期値設定の部分がindex out of rangeになる
可能性があるので注意
"""
######################################################
S = INT()
dp = [0]*(S+1)
dp[0] = 1
dp[1] = 0
if S>=2:#このミスまたやった！！！！！！！！
    dp[2] = 0
for i in range(3,S+1):
    dp[i] = dp[i-1]+dp[i-3]
    dp[i] %= mod
print(dp[S]%mod)
