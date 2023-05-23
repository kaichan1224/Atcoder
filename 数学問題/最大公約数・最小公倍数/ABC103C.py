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
994 518 941 851 647 2 581
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
気づけるかどうかがポイント
最適解をまず考えることが大事
m mod aは最適解はa-1で全ての場合で最適解になる場合はそれぞれの最大公約数であるが
計算する必要はない。
"""
#--------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))
print(sum(A)-len(A))










