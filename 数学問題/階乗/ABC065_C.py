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
100000 100000

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
並び替え問題

"""
#--------------------------------------------------------------
N,M = MAP()
if abs(N-M)>1:
    print(0)
elif N==M:
    print(math.factorial(N)*math.factorial(M)*2%mod)
else:
    print(math.factorial(N)*math.factorial(M)%mod)