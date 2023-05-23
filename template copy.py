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
5
8
1 1 1
1 2 4
1 1 4
2 4
1 1 4
2 4
3 1
3 2
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
N = INT()
Q = INT()
box = defaultdict(int)
for _ in range(Q):
    query = LIST()
    if query[0]==1:
        i,j = query[1],query[2]
        box[j].append(i)
    elif query[0]==2:
        i = query[1]
    else:
        i = query[1]
print(box)



        





