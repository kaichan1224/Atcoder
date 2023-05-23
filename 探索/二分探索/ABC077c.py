import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_left,bisect_right
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

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・DPを使いそう？→時間的に間に合わない

<ポイント>
3つ要素があるときは真ん中を固定する(全探索する)
→残り2つは二部探索で範囲を求めることができる
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
A.sort()
B = LIST()
B.sort()
C = LIST()
C.sort()
#bを全探索する
ans = 0
for b in B:
    acnt = bisect_right(A,b-1)
    ccnt = N-bisect_left(C,b+1)
    ans += acnt*ccnt
print(ans)










