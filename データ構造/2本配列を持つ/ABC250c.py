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
10 6
1
5
2
9
6
6

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・配列を2つ持って管理する
b[ボール]=i番目
a[i番目]=ボール


"""
#--------------------------------------------------------------
N,Q = MAP()
a = []#ボールの数字
b = []#ボールの位置
for i in range(N):
    a.append(i)
    b.append(i)
for i in range(Q):
    x = int(input())
    x -= 1
    #ボールの位置
    now = b[x]
    if now==N-1:
        irekae = now-1
    else:
        irekae = now+1
    b[a[now]] = irekae
    b[a[irekae]] = now
    a[now],a[irekae] = a[irekae],a[now]
for i in a:
    print(i+1,end=' ')
    

    






