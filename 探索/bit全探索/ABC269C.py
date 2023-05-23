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
11
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>


<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N = INT()
N2 = format(N,"b")
ans = []
#何番目に1があるか
#左からn個目の1は何番目か
d = defaultdict(int)
tp = 0
for i in range(len(str(N2))):
    if str(N2)[len(str(N2))-i-1]=="1":
        d[tp] = len(str(N2))-i-1
        tp += 1
cnt = len(d)
for bits in product([0,1],repeat=cnt):#正直者だと仮定する
    tmp = ["0"]*(len(str(N2)))
    for idx,b in enumerate(bits):
        if b==1:
            tmp[d[idx]] = "1"
    a = "".join(tmp)
    ans.append(int(a,2))
ans.sort()
for i in ans:
    print(i)
            
    