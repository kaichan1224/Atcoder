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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3 3
1 2 3
2 3 1
1 2 -1
1 3 2

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
階差を考える
"""
######################################################
N,Q = MAP()
A = LIST()
#Aの階差
B = [A[i+1]-A[i] for i in range(N-1)]
BS = 0
#不便さ
for i in range(N-1):
    BS += abs(B[i])

for _ in range(Q):
    l,r,v = MAP()
    l,r = l-1,r-1
    if l-1>=0:
        BS -= abs(B[l-1])
        B[l-1] +=v
        BS += abs(B[l-1])
    if r<N-1:
        BS -= abs(B[r])
        B[r] -=v
        BS += abs(B[r])
    print(BS)


    










