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
3 3
142857
004159
071028
159
287
857


"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
N,M = MAP()
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
cnt = 0
for s in S:
    flag = False
    for t in T:
        if s[3:] == t:
            flag = True
    if flag:
        cnt += 1
print(cnt)




