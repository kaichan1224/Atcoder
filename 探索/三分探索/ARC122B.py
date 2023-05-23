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
3
3 1 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""

"""
#--------------------------------------------------------------
N = int(input())
A = list(map(int,input().split()))

#最小にしたい関数fを定義する
def f(x):
    tmp = 0
    for i in range(N):
        tmp += x + A[i] - min(A[i],2*x)
    return tmp/N

#関数fの最小値を探したい区間の両端を設定する
left = 0
right = 10**9

#誤差を下回るまでwhile文を回す
def totu_search(low,high):
    while high - low >1e-6:#誤差
        mid_left = high/3+low*2/3
        mid_right = high*2/3+low/3
        if f(mid_left) >= f(mid_right):
            low = mid_left
        else:
            high = mid_right
    ans = low
    return ans
#その時のf(t)の値←今回求めるのはこっち
print(f(totu_search(left,right)))


