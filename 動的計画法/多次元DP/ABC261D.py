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
6 3
2 7 1 8 2 8
2 10
3 1
5 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<動的計画法について復習>
・まとめられる処理をまとめて、同じ計算を行わないようにする
・探索の拡張と考える（重要）
・DPはpypy

<落とし穴１>
・なにか規則性を見つけて「正しい選び方の法則」のようなものを見つけようとしがち
→すべて探索することが大切、単純に探索すると計算時間が間に合わない場合は、
どのように計算結果をまとめていくかを考えるとよい

<問題の要約>
・N回コイントスする
・表→カウント+1してXi円貰う
・裏→カウンタ=0にして0円貰う
・M種類のボーナスがあり、カウンタCiになるたびにYi円もらえる
・最大何円もらえるか

<ポイント>
・DPで重要なことは、遷移前の情報は既に計算済みであること
→つまり、それ以降の要素によって内容は変化しない必要がある
・今回は、i回目時点で、とあるカウンタ数値のお金の最大値はそれ以前の要素によって変化しない
→dp[i回目][カウンタc]として遷移を考えていけば良い
（これが、探索の計算結果をまとめるということである!）
"""
#--------------------------------------------------------------
N,M = MAP()
X = LIST()
d = defaultdict(int)
for _ in range(M):
    c,y = MAP()
    d[c] = y
#dp[i回目][カウンタ]
dp = [[0]*(N+1) for _ in range(N+1)]
#n回目のトスコイン
for n in range(1,N+1):
    for c in range(n+1):
        #カウンタが0のときは、一個前が裏であるということである
        #よって、カウンタが0のときの最大値は、前の回の最大値を取ってくれば良い。
        if c == 0:#
            dp[n][c] = max(dp[n-1])
        else:
            dp[n][c] += dp[n-1][c-1] + X[n-1] + d[c]
print(max(dp[N]))
