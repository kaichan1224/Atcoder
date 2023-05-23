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
"""
<ポイント>
・条件を満たすものを構築して出力せよ→ある種のひらめきを要求する問題
・N進数→1桁以上d桁以下のp進表記を用いるとp^d-1以下のすべての非負整数を表現できる


"""
#--------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(1,100):
    ans.append(i)
for i in range(100,10000,100):
    ans.append(i)
for i in range(10000,1000000,10000):
    ans.append(i)
print(len(ans))
print(*ans)







