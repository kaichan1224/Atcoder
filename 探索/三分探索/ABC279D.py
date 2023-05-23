import io
import sys
import math
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
1000000000000000000 100
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""


"""
#-------------------------------
def f(i):
    if i==-1:
        return float("inf")
    return B*i+A/math.sqrt(i+1)

A,B = MAP()

#関数fの最小値を探したい区間の両端を設定する
left = 0
right = 10**18

#誤差を下回るまでwhile文を回す
def totu_search(low,high):
    while high - low >1e-3:#誤差
        mid_left = high/3+low*2/3
        mid_right = high*2/3+low/3
        if f(mid_left) >= f(mid_right):
            low = mid_left
        else:
            high = mid_right
    ans = low
    return ans
#その時のf(t)の値←今回求めるのはこっち
tmp = totu_search(left,right)
num1 = int(tmp)
num2 = num1-1
num3 = num1+1
ans = min(f(num1),f(num2),f(num3))
print(ans)

