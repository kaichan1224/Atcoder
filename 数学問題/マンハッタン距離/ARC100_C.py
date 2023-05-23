import io
import sys
#sys.setrecursionlimit(10**7)
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
5
2 2 3 5 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・式変形できる部分を考える
→abs(A1-(b+1))+abs(A2-(b+2))+...
→abs((A1-1)-b)+abs((A2-2)-b)+...
・マンハッタン距離の差の総和を最小化するときは中央値を使う
→Σ|x-d|を最小化→dはXの中央値
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
ans = 0
B = []
for i in range(N):
    B.append(A[i]-(i+1))
B.sort()
#print(B)
b = B[N//2]
for i in range(N):
    ans += abs(A[i]-(b+(i+1)))
print(ans)






