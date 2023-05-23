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
7
1 2 5 5 2 3 1
2
3 5
4 6

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・各日において1-ld,rd+1-N号室の人数の最大値をO(1)orO(logN)で求めないといけない

<キーワード>
・累積的に考えるテクニック
・累積max
・右からの累積と左からの累積をそれぞれ考えるテクニック

<ポイント>
・わからない時は、一旦全探索解を書いてみること
→計算量を改善するところが見つかるかも
・累積的にmax,minを求めることでうまくいく問題も

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
D = INT()
Lruiseki = [0]*N
Rruiseki = [0]*N
Lruiseki[0] = A[0]
Rruiseki[N-1] = A[N-1]
#左からの累積max
for i in range(N-1):
    Lruiseki[i+1] = max(Lruiseki[i],A[i+1])
#右からの累積max
for i in range(1,N)[::-1]:
    Rruiseki[i-1] = max(Rruiseki[i],A[i-1])

for i in range(D):
    l,r = MAP()
    l,r = l-1,r-1
    print(max(Lruiseki[l-1],Rruiseki[r+1]))