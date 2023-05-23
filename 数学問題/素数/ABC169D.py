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
997764507000
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
・素因数分解して小さい要素から1,2,3,..ずつ使っていけば良い。
・「N=10**12はO(√N)だと10**6」のメタ読みは重要!
"""
#--------------------------------------------------------------
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

N = INT()
nums = factorization(N)
ans = 0
for a,b in nums:
    if a==1:
        continue
    tmp = 1
    while True:
        b -= tmp
        if b < 0:
            break
        tmp += 1
        ans += 1
print(ans)
    
