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
4
4 20
3 30
2 40
1 10
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・iをPiより早く取り除いたらAi点獲得
・右端or左端のどちらかを全てのブロックがなくなるまで取り除くことができる
・合計得点としてあり得る最大値を求める

<キーワード>
・区間DP
-dp[l][r] := 区間 [l,r)について、最適な状況下での何かしらの値を考える時に使う
-遷移の方法として典型なのが、
1.左端と右端の一つが変化する:dp[l][r] = dp[l+1][r]とdp[l][r-1]から更新するもの
2.二つの区間を組み合わせて新しいものを得る:dp[l][r]:全てのiについてdp[l][i],dp[i][r]
の２パターン
-使用する場面としては
1.区間の除去、圧縮、合体などが生じるとき
2.O(N^2),O(N^3)が間に合いそうなとき

<ポイント>
・DP問題の基本に立ち返って問題を解いてみる
1.DPテーブル
-dp[l][r]:区間l,rにおける得点の最大値
-区間の幅は約N=2000なのでO(N^2)で十分間に合う

2.初期値について
-dp[l][r]は区間[l,r]が残っている時の得点と考えると、
dp[1][N]:区間1~N(つまり全て)が残っている時の得点は当然0
↓
-dp[l][r]:区間1~Nを取り除いた時の得点
(このようにしないとメモ化再帰で求めることができない)

3.dpの遷移について
-遷移の書き方について、注意が必要。というのも遷移に少しクセがあるからである
-forループで書く場合は少し注意が必要ならそれを気にしたくないならメモ化再帰で書くと楽?

-dp[l][r]:[l,r]が残っている時の点数の最大値
-dp[l][r] = max(dp[l-1][r]+PA[l][1]) (lをとるがPA[l][1]より先に取り除いた場合)
-dp[l][r] = max(dp[l][r+1]+PA[r][1])
??????

-dp[l][r]:l~r取り除いた時の最大値として考えるみるのは?
dp[l][r] = dp[l+1][r]+PA[l][1],dp[l][r-1]+PA[r][1]

AC!

"""
#--------------------------------------------------------------
N = INT()
PA = [[0,0]]
for _ in range(N):
    p,a = MAP()
    PA.append([p,a])
dp = [[-INF]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][i] = 0

#区間l~rを取り除いた時の最大値
def memo(l,r):
    if dp[l][r]!=-INF:
        return dp[l][r]
    if l==r:
        return 0
    if (l+1<=PA[l][0]<=r):
        dp[l][r] = max(dp[l][r],memo(l+1,r)+PA[l][1])
    else:
        dp[l][r] = max(dp[l][r],memo(l+1,r)+0)
    if (l<=PA[r][0]<=r-1):
        dp[l][r] = max(dp[l][r],memo(l,r-1)+PA[r][1])
    else:
        dp[l][r] = max(dp[l][r],memo(l,r-1)+0)
    return dp[l][r]
ans = memo(1,N)
print(ans)
        

        
    
        