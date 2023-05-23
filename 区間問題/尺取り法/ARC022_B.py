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
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
from bisect import bisect_left,bisect_right
#--------------------------------------------------------------
_INPUT = """\
1
100

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
同じ味のブロックが2つ以上含まれない、つながった部分
→連続部分列について、同じ種類のものを含まない場合の最長の長さ
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
q = deque()
d = defaultdict(int)
ans = 0
for c in A:
    q.append(c)
    d[c] += 1
    #print(q)
    #print(d)
    while q and not(len(d)==len(q)):
        rm = q.popleft()
        if d[rm]>=2:
            d[rm] -= 1
        else:
            d.pop(rm)
    ans = max(ans,len(q))
print(ans)








