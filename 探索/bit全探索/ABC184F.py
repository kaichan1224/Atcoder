import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_left,bisect_right
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
6 100
1 2 7 5 8 10



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・半分全列挙で解けそう
・2分探索のindexがうまく合わないのでmeguru式を使う?

<その後>
・bisect.rightを使えば-1することでちゃんと動作する(とりあえず動けば何でもいいです)
"""
#--------------------------------------------------------------
N,T = MAP()
A = LIST()
A1 = []
A2 = []
for i in range(N):
    if i%2==0:
        A1.append(A[i])
    else:
        A2.append(A[i])
a1list = []
a2list = []
for bits in product([0,1],repeat=len(A1)):
    cnt = 0
    for i in range(len(A1)):
        if bits[i]==1:
            cnt += A1[i]
    if cnt<=T:
        a1list.append(cnt)

for bits in product([0,1],repeat=len(A2)):
    cnt = 0
    for i in range(len(A2)):
        if bits[i]==1:
            cnt += A2[i]
    if cnt<=T:
        a2list.append(cnt)   
a2list = list(set(a2list))
a1list = list(set(a1list))
a2list.sort()
ans = 0
for i in a1list:
    idx = bisect_right(a2list,T-i)-1
    ans = max(ans,i+a2list[idx])
print(ans)









