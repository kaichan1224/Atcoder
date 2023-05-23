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
6 6
1 2 3 4 5 6
"""
sys.stdin = io.StringIO(_INPUT)
N,X = MAP()
P = LIST()
for k,p in enumerate(P):
    if p==X:
        print(k+1)