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
10
3 9 6 1 7 2 8 0 5 4

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>
・視点を変える

<ポイント>
・人ではなく料理に着目する
・何回回せば喜ぶのかを求めて、その前後回数,回した時も喜ぶ☜ここ重要!!!!!
"""
#--------------------------------------------------------------
N = INT()
P = LIST()
#i番目の料理が人qiの前においてある
q = [0]*N
for i in range(N):
    q[P[i]] = i

#i回回した時に喜ぶ人の数
t = [0]*N
for i in range(N):#i番目の料理について
    k = (i-q[i])%N #何回回せば喜ぶのか(目の前にくるのか)
    t[k] += 1
    t[(k-1)%N] += 1
    t[(k+1)%N] += 1
print(max(t))
    
    
    