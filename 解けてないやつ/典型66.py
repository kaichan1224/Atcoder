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
<転倒数>
・左から順番に、自分より左にいるのに自分より大きい数の個数
・普通に求めたかったらバブルソートをすればよいが計算量はO(N^2)
・BITを用いるとO(NlogN)で求めることができる






"""
#--------------------------------------------------------------
N = INT()
LR = [LIST() for i in range(N)]





