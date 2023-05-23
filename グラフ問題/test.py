from asyncio.windows_events import NULL
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
inf=float('inf')
###################################################
_INPUT = """\
"""
sys.stdin = io.StringIO(_INPUT)
###################################
