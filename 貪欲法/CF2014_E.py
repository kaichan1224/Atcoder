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
#--------------------------------------------------------------
_INPUT = """\
1
2 

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
前の値と違うかどうかを記録したいときはflag管理するのもいいが
prevで管理するほうが早い

<考察>
* 注意:差分が0の回はカウントする必要がない
* 直前と違うかどうかを管理するだけでいいので前回の値を記録すれば良い
"""
#--------------------------------------------------------------
N = INT()
R = LIST()
a = []

for i in range(N-1):
    diff = R[i+1]-R[i]
    if diff>0:
        a.append(1)
    elif diff<0:
        a.append(-1)
cnt = 1
prev = 0 
for d in diff:
    if d!=prev:
        cnt += 1
    prev = d

if cnt>=3:
    print(cnt)
else:
    print(0)





