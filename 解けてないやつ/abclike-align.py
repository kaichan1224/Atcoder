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
6
3
1
4
1
5
9

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・好きな順に一列に並べる時、隣ある要素の差の合計の最大値を求める
・ソートして端と端の値をとってみる(エスパー)

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
A = [INT() for _ in range(N)]
ans = 0
Asort = deque(sorted(A))
Asort2 = deque(sorted(A))
newA = []
newA2 = []
for i in range(N):
    if i%2==0:
        newA.append(Asort.popleft())
        newA2.append(Asort2.pop())
    else:
        newA.append(Asort.pop())
        newA2.append(Asort2.popleft())
ans1 = 0
ans2 = 0
for i in range(N-1):
    ans1 += abs(newA[i+1]-newA[i])
    ans2 += abs(newA2[i+1]-newA2[i])
print(ans1,ans2)
    