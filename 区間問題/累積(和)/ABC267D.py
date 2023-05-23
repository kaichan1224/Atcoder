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
1 1
100





"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・ずらしながら差分をうまく計算して求める

<キーワード>
・差分計算と累積和を使うわりかし典型なやつ

<ポイント>
・答えの初期値に注意する!(これを忘れていたせいで1WA)
"""
#--------------------------------------------------------------
N,M = MAP()
A = LIST()
Asum = [0]+list(accumulate(A))
ans = -INF
start = 0
for i in range(M):
    start += A[i]*(i+1)
ans = start #これを忘れていたせいで1WA!
for i in range(M,N):
    tmp = start
    tmp -= Asum[i]-Asum[i-M]
    tmp += A[i]*M
    ans = max(tmp,ans)
    start = tmp
print(ans)


