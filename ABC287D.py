import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
a?c
b?

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
"""
文字ごとにsetで考えればいける?
"""
S = input()
T = input()
td = 
for x in range(len(T)+1):
    pre = S[:x]
    back = S[len(S)-len(T)+x:]
    
    





