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
1
For


"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
N = INT()
yes = 0
no = 0
for _ in range(N):
    s = input()
    if s == "For":
        yes += 1
    else:
        no += 1
if yes>no:
    print("Yes")
else:
    print("No")




