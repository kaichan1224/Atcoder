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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
8 4
15 15 15 15 15 15 15 15
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・mod Mの配列で管理する
・考え方は和がMと同じ感じ
・a-b = Mk a-b=M (modM)a全探索してb=a-M


"""
#--------------------------------------------------------------
N,M = MAP()
A = LIST()
modM = [0]*M
for a in A:
    modM[a%M] += 1
ans = 0
for a in A:
    a %= M
    b = (a-M)%M
    if a==b:
        ans += max(0,modM[b]-1)
    else:
        ans += modM[b]
print(ans//2)
    