import io
import sys
sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
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
2 7

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
メモ化再帰で構造を作る→長さがだいたい倍になるので2^50で到底間に合わない

<ポイント>
f(level, x) := レベルlevelバーガーの下からx番目まででパティが何枚あるか
（xは0-indexed）
を考える。

"""
#--------------------------------------------------------------
N,X =  MAP()
memo = ['']*(N+1)
memo[0] = 'P'

def make(N):
    if memo[N]!='':
        return memo[N]
    memo[N] = 'B'+make(N-1)+'P'+make(N-1)+'B'
    return memo[N]

ans = make(N)
cnt = 0
for i in range(0,X):
    if ans[i]=='P':
        cnt += 1
print(cnt)






