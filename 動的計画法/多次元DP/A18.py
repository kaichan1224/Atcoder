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
3 7
2 2 3

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・bit全探索だとN=22ぐらいまでだから部分点は取れるけどN=60
・bitDP or 半分全列挙とか
これは良くない思考です
・制約N=60とか50でもdpテーブルを普通に作れることがあるのですぐにbitDPだとか
変な方向に走らないように!!!!

<キーワード>
・典型的なDP(部分和問題)

<ポイント>
・DPは最大値、最小値、数え上げ以外に存在判定にも使えるよ!!!!
・遷移の条件式は細かいところだけど丁寧にやりましょう!!!

<ミスポイント>
・最後の条件を満たすかどうかの判定の部分でミスっていた
-Sを満たすかは1~Nの全てでチェックする必要がある!
・初期条件の設定が甘かった
-dp[0][0]だけではなく全ての1~NでTrueにしておく必要がある!!(やっぱないかも?)
・選択しない場合でs+A[i]<=Sの部分を満たさない時の遷移が抜けていたためWA!
-条件分岐は細かく!!

"""
#--------------------------------------------------------------
N,S = MAP()
A = LIST()
dp = [[False]*(S+1) for _ in range(N+1)]
for i in range(N+1): 
    dp[i][0] = True
for i in range(N):
    for s in range(S+1):
        #選択する場合
        if dp[i][s] and s+A[i]<=S:
            dp[i+1][s+A[i]] = True
        #選択しない場合
        if dp[i][s]:
            dp[i+1][s] = True
flag = False
for i in range(1,N+1):
    if dp[i][S]:
        flag = True

if flag:
    print("Yes")
else:
    print("No")

