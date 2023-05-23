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
2
5 18

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
・エスパーして全部の最大公約数を出力したらAC
・ときにはエスパーも大事
・複数の最大公約数の求め方

"""
#--------------------------------------------------------------
N = int(input())
A = LIST()
a = math.gcd(A[0],A[1])
for i in range(2,N):
    a = math.gcd(a,A[i])
print(a)





