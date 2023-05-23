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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
5
4 10 6 3
6 5 4 3
1 1 0 0
31415 92653 58979 32384
1000000000 1000000000 999999999 999999999
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
floor_sum:自然数m,整数a,b,0以上の整数nに対して
sum(i=0→n-1)floor((ai+b)/m)の計算
愚直にやるとTLE

"""
######################################################

#floor_sumは格子点の数え上げ問題に帰着出来る
def floor_sum(n, m, a, b):#a,bが負の場合も対応
    ans = 0
    while True:
        if a >= m or a < 0:
            ans += n * (n - 1) * (a // m) // 2
            a %= m
        if b >= m or b < 0:
            ans += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m: break
        n, b, m, a = y_max // m, y_max % m, a, m
    return ans   

T = INT()
for _ in range(T):
    N,M,A,B = MAP()
    print(floor_sum(N,M,A,B))



