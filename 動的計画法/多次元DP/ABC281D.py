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
3 1 2
1 3 5


"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
・K番目までをmodDで見ていくところまではあっている
・多次元DP

<ポイント>
・Aについてi番目"まで"を選んだ時について考えると良い
・「先頭i項のうち」のDP
・一旦配るDPを考えることにする

・DP配列(テーブル)ではi番目までの結果がわかる
・遷移の時はi番目を見ている

<つまづいたところ>
・DPテーブルでは、配列の部分ではi番目まで~がわかり、
遷移は基本的に点で考える
・DPでは注目しているものについて、選ぶ場合、選ばない場合それぞれの遷移を考える必要があるので注意
・そもそもDPで埋まっていない部分はスキップして良い(遷移もとがない場合)
・遷移の順番が大事
"""
#-------------------------------
N,K,D = MAP()
A = LIST()
#dp[i][j][k]:=先頭i項のうち、j項を足し合わせた和(mod D)がkである時の最大値
#DP[i][c][r]=i番目まででc個選んで、和をDで割ったあまりがrになるような最大値
dp = [[[-1 for i in range(D)] for j in range(K+1)]for _ in range(N+1)]
dp[0][0][0]  = 0
for j in range(K+1):
  for i in range(N):#i番目を見ている
    for k in range(D):
      #あり得ない場合はスキップ
      if dp[i][j][k] == -1:
        continue
      #選ばない場合
      #今見ているのはAi番目で、選ばない場合はi+1番目のテーブルが埋まる
      dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k])
      if j != K:
        dp[i+1][j+1][(k+A[i])%D] = max(dp[i+1][j+1][(k+A[i])%D], dp[i][j][k] +A[i])
print(dp[N][K][0])







