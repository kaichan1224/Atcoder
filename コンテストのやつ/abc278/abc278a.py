import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
3 2
2 7 8
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""

"""
#-------------------------------
N,K = MAP()
A = LIST()
a = deque(A)
for _ in range(K):
    a.popleft()
    a.append(0)
print(*a)
