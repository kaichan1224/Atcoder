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
5
1 1 2 1 2


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・Counter + 累積和　で前処理

<ポイント>
・全体から引くだけの処理しかしていないので、累積和は考える必要がない

・クエリ問題の方針
1.各クエリについて高速に計算
2.全部前計算
3.差分を計算することで高速に計算　←今回はこれ
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
counter = [0]*(N+1)
counter_pre = [0]*(N+1)
for a in A:
    counter[a] += 1

for i,a in enumerate(counter):
    if a==0 or a==1:
        counter_pre[i] = 0
    elif a==2:
        counter_pre[i] = 1
    else:
        counter_pre[i] = a*(a-1)//2

counterSum = list(accumulate(counter_pre))

for i,a in enumerate(A):
    ans = counterSum[N]-counter_pre[a]
    tmp = counter[a]-1
    if tmp==0 or tmp==1:
        ans += 0
    else:
        ans += tmp*(tmp-1)//2
    print(ans)






