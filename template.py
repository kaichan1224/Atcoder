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
4
oo--

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
N = INT()
S = input()
flag1 = False
flag2 = True
for s in S:
    if s=="o":
        flag1 = True
    elif s=="-":
        pass
    else:
        flag2 = False
if(flag1 and flag2):
    print("Yes")
else:
    print("No")




