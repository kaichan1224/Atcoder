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
3 10

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<ポイント>
回数の期待値DPの形
・dp[i] =(dp[何か]+(回数))*(確率)+(dp[何か]+(回数))*(確率)+...
・Nターンあったら、各ターンは別々に期待値が計算できたりする
・状態遷移を表すグラフを作ることができれば、期待値についての立式をすることができる

<注意>
答えに影響が出るもので、割り算があるときにmodを取る必要がある時はフェルマーのやつ
を使う必要がある
"""
#-------------------------------
def division_mod(a,b,mod):#a//b%modを正確に求める関数
    return a*pow(b,mod-2,mod)%mod
N,P = MAP()
mod = 998244353
dp = [0]*(N+1)
dp[1] = 1
for i in range(2,N+1):
    dp[i] = (dp[max(i-2,0)]+1)*(division_mod(P,100,mod))+(dp[max(i-1,0)]+1)*(1-(division_mod(P,100,mod)))
    dp[i] %= mod
print(dp[N]%mod)

