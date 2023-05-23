import io
import sys
import math
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
869121
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
包除原理：解ける数え上げの範囲を広げることが出来る
余事象を考えるのは重要！
"""
######################################################
N = INT()
ans = pow(10,N,mod)-(pow(9,N,mod)*2-pow(8,N,mod))
print(ans)


