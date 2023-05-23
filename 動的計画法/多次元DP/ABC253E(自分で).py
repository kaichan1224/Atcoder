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
1000 5000 0



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・問題概要:
長さNの配列であり、大きさが1~M,配列間の差がabs(Ai-Ai+1)>=Kのものという条件を
満たす配列の個数は何通りあるか
→何通りかを求める問題といえば、DPでいけそう(制約的にも)
制約から二次元DPまでいけそう

DP問題?を解く(流れに沿って)
・dp[i][m]:配列のi番目の大きさがmの時何通りあるか
・遷移を考える
・貰うDPで一旦考えてみる。
dp[i][m] += dp[i-1][1~m-K and m+K~M]でいけそう
それぞれのdp[i][m]を調べるのにオーダーO(N^2)で、遷移にO(N)掛かると制約オーバー:(
→遷移の部分をどうにかしてO(1)にしたい。
→累積和をうまく使えないか考える
アイデア
・dp[i][m]列目の処理が終わった段階で、累積和をとる(新たなDP配列を作る(DP2としてみる))→その必要もないかも?
・dp[i-1][1~M-K]はdp[i-1][M-K]一発、dp[i-1][m+K~M]はdp[i-1][M]-dp[i-1][m+K-1]で行けるのでは?
→これにより、累積和をうまく使うことにより遷移の部分をO(1)で処理できるので、全体をO(NM)で解くことが可能になった
実装しましょう

・2WAでた!どこやねん
(ここからはヒントを見た)
・結論から言うとコーナーケースを見逃していた
・K=0の時、本来では、全ての範囲で遷移が可能なので
dp[i][m] += dp[i-1][1~M]
累積和を使った遷移はdp[i][m] += dp[i-1][M]となる
ここで、K=0でない場合の遷移にK=0を代入してみると、
dp[i][m] += dp[i-1][m] + dp[i-1][M] - dp[i-1][m-1]
         (=dp[i-1][m]の部分+dp[i-1][M])
となってしまっているのでこれはおかしい。
よってK=0の場合を別に用意しておく必要がある

<TIPS>
・1~2WAが出ている場合は、コーナーケースの見落とし等を一番に考える。
(今回はK=0の場合を見逃していた)
・累積和の部分で分割する場合と分割しない場合をセットで考えることはできない

<point>
・遷移をよく見ると区間和になっているDP→累積和を求めておくと高速化できる
・累積和で高速化する場合は[貰うDP]で考える!!!!!
・ある範囲からある範囲までの値を貰うときに貰う部分のDPの値の累積和を計算しておく
→先に累積和を求めておくと計算量を減らすことができる
→遷移の数をM→1に大きく減らすことができる
"""
#--------------------------------------------------------------
N,M,K = MAP()
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,M+1):
    dp[1][i] = 1
#累積和取り方(2~N)まで累積和取ればいい
for i in range(2,M+1):
    dp[1][i] += dp[1][i-1]
for i in range(2,N+1):
    #遷移
    for m in range(1,M+1):
        if K==0:
            dp[i][m] += dp[i-1][M]
        else:
            if m-K>=0:
                dp[i][m] += dp[i-1][m-K]
            if m+K<=M:
                dp[i][m] += dp[i-1][M]-dp[i-1][m+K-1]
            dp[i][m] %= mod
    #累積和をとる
    for m in range(2,M+1):
        dp[i][m] += dp[i][m-1]
        dp[i][m] %= mod
print(dp[N][M]%mod)
        
