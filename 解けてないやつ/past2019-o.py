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
2
1 2 3 4 5 6
7 8 9 10 11 12

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
最大化するためには、今現在で1番小さい手を取るように選択していく必要がある

回数の期待値DPの形
・dp[i] =(dp[何か]+(回数))*(確率)+(dp[何か]+(回数))*(確率)+...
・Nターンあったら、各ターンは別々に期待値が計算できたりする
・状態遷移を表すグラフを作ることができれば、期待値についての立式をすることができる
"""
#-------------------------------
import heapq
N = INT()
A = [LIST() for _ in range(N)]
now = []
for i in range(N):
    now.append((min(A[i]),i))
heapq.heapify(now)
dp = [0]*(6*N+1)
def dp(i):
    if i==0:
        return 0
    num,idx = heapq.heappop(now)
    res = 0
    for b in range(A[idx]):
        if num>b:
            res += dp(idx)*





