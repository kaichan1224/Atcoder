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
4
13 13
7 11
7 11
2017 2017
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・解法1 O(QlogN)
2017に似たリストを作る→2分探索

・解法2 O(Q)
2017に似た表を作る→累積和で区間の個数を高速に求める

”区間の個数や総和は表作って累積和でクエリを高速に処理可能”
"""
#--------------------------------------------------------------
def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True
Q = int(input())
a = []
for i in range(1,10**5+1,2):
    if isprime(i) and isprime((i+1)//2):
        a.append(i)
for i in range(Q):
    l,r = MAP()
    ans = bisect_right(a,r)-bisect_left(a,l)
    print(ans)








