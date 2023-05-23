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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
4 2 3
1 0
2 0
1 1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・集合のandは&で!
・gridでシュミレーションするとH,W>=2*10**5より、計算量が爆発
→setで管理する!

<180度回転>
(x,y)→(x+H-1,y+W-1)
"""
#--------------------------------------------------------------
H,W,N = MAP()
now = set()
nxt = set()
XY = [LIST() for _ in range(N)]
for x,y in XY:
    now.add((x,y))
    nxt.add((H-1-x,W-1-y))
ans = now & nxt
print(len(ans))
