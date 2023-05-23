import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#--------------------------------------------------------------
"""
<考察>
・所謂区間スケジューリング問題では?
-期限が短いやつでかつかかる時間が短い問題から解いていくという方針。
→7WAでた

別の方針を考えてみる
・Ti,Diが極端に小さい→二次元ぐらいのDPだったら解ける範囲
・dp[i]:i分

<キーワード>
・問題を解く上でのポイント
-少しずつヒントを見つけていく
・問題設定を変えて考えてみる

<ポイント>
・問題設定を変えてヒントを得る
-今回の問題では、最大で何問正解できるかではなく最後の問題まで到達することができるかという簡単な設定を考える
・すると、最後の問題まで到達することができるかは問題を順番にみてDPすればいけそうだとわかり、
・何分,i問目の地点で何問解けているかのDPを考えていきたくなる
・問題を解くか解かないかの遷移ができ、また問題の締め切りが小さい順に当然したくなるため、ソートする必要も出てくるだろう

このように問題設定を変えてみるとヒントが出てきたり、今まで解いたことのあるような問題を似た問題に置き換えることができるように
なるだろう。
・選択するか否か

<再び考察>
・dp配列の定義は?
・dpの遷移は配るか貰うか --> 配るDPで
・遷移式は?
"""
#--------------------------------------------------------------
N = INT()
TD = [LIST() for _ in range(N)]
#(かかる時間、締め切り)
TD.sort(key = lambda x:x[1])
Dmax = TD[N-1][1]
#dp[N][D]:n問目,D分時点で解けている問題の数の最大値
dp = [[0]*(Dmax+1) for _ in range(N+1)]
#i問目の地点で
for i in range(N):
    for m in range(Dmax+1):
        #締め切り以内だったら選択するという選択を取ることができる
        if m+TD[i][0]<=TD[i][1]:
            dp[i+1][m+TD[i][0]] = max(dp[i][m]+1,dp[i+1][m+TD[i][0]])
        #選択できなかったら
        dp[i+1][m] = max(dp[i][m],dp[i+1][m])
ans = 0
for i in range(N+1):
    for j in range(Dmax+1):
        ans = max(ans,dp[i][j])
print(ans)

        
        
    