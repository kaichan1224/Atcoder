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
3 4 6 3 3 7




"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・全探索の計算量改善
有意に値が決まるときは全探索する必要がない!!!(茶diffだと重要)
→3*3を2*2に落とすことができるので、計算量的にはO(N^9)→O(N^4)で間に合う
"""
#--------------------------------------------------------------
h1,h2,h3,w1,w2,w3 = MAP()
ans = 0
for a in range(1,31):
    for b in range(1,31):
        for d in range(1,31):
            for e in range(1,31):
                c = h1-a-b
                f = h2-d-e
                g = w1-a-d
                h = w2-b-e
                i = w3-c-f
                if min(c,f,g,h,i)>0 and g+h+i==h3 and c+f+i==w3:
                    ans += 1
print(ans)
            





