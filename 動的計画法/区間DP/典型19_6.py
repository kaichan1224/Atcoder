import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from functools import lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
15
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<問題内容>
長さ2Nの正整数列
1<=i<Mの中で1つ選びAi,Ai+1を取り除くことを繰り返す
取り除くコストは|Ai-Ai+1|,N回操作を繰り返すときにかかるコストの総和の最小値

<考察>
*貪欲に取り除いていくといける?→無理

<ポイント>
*列の操作は区間DP
*使われそうな場面について
1,区間の除去・圧縮・合体が生じる時
2,O(N^2)orO(N^3)が間に合う時
*区間DPの扱い方
dp[l][r]:区間l-rについて最適な状況下での何かしらの値
*dpの更新
O(N^3)の問題だと、
dp[l][r] = 全てのiについてdp[l][i]とdp[i][r]を確認して更新
O(N^2)の問題だと,
dp[l][r] = dp[l+1][r]とdp[l][r-1]から更新
*書き方
再帰で各方法とボトムアップ(for文)で書く方法の2つがあるが、
for文で配列の更新処理を行おうとすると難しい事が多いので
メモ化再帰を利用すると実装しやすくなってよい。
*注意
区間領域に注意する
dp[l][r] := 区間 [ l, r ) について、最適な状況下での何かしらの値
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
@lru_cache(None)
def dp(l,r):#dp[l][r]:l～rの人が抜けた時の最小コスト
    if l==r:#同じ時はありえないので0
        return 0
    #lとrの人が抜けるとき(つまり最後のとき)    
    res = abs(A[l]-A[r-1])+dp(l+1,r-1)
    for k in range(l+2,r,2):#区間を分けて考える(間の人が抜けたとき)
        res = min(res,dp(l,k)+dp(k,r))
    return res                                   
print(dp(0,2*N))









