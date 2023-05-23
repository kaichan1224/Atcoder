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
3 1 4 1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・条件の言い換え
1<=i<j<k<=N and Ai,Aj,Akは異なる→
→Ai<Aj<Akを満たす組(Ajを大小関係の真ん中だと一般化しても問題なし)
→細かく言うと、Aの中から3つ異なる数字を選んだらそれの大中小は位置に決められるから、
それに合わせて、小さいものから添字をi,j,kにすると、これがもとの条件をおなじになる。
・真ん中を固定
・余事象
"""
#--------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))
cnt = 0
maxa = max(A)
acnt = [0]*(maxa+1)
for a in A:
    acnt[a] += 1
acnt = list(accumulate(acnt))
for j in range(N):
    cnt += acnt[A[j]-1]*(acnt[maxa]-acnt[A[j]])
print(cnt)






