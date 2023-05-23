import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
5
1100 1900 2800 3200 3200



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
場合分けに注意!


"""
#--------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))
d = defaultdict(int)
cnt = 0
for a in A:
    if 1<=a<=399:
        d[0] += 1
    elif 400<=a<=799:
        d[1] += 1
    elif 800<=a<=1199:
        d[2] += 1
    elif 1200<=a<=1599:
        d[3] += 1
    elif 1600<=a<=1999:
        d[4] += 1
    elif 2000<=a<=2399:
        d[5] += 1
    elif 2400<=a<=2799:
        d[6] += 1
    elif 2800<=a<=3199:
        d[7] += 1
    else:
        cnt += 1
if cnt==0:
    print(len(d),len(d))
else:
    if len(d)==0:
        print(1,cnt)
    else:
        print(len(d),len(d)+cnt)





