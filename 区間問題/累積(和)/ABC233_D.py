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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
6 5
8 -3 5 7 0 -4
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
区間の和→累積和を考えるは定番of定番!!!!

連想配列で計算量を減らす工夫
"""
###################################################
N,K = MAP()
A = LIST()
Asum = [0]
for i in range(N):
    Asum.append(Asum[i]+A[i])
ans = 0
print(Asum)
d = defaultdict(int)
for l in range(1,N+1):
    #Asum[r]-Asum[l-1]==Kの数を数えたい
    #Asum[l-1]の出現回数をメモして、A[sum[r]]-Kの個数を数えれば良い
    d[Asum[l-1]] += 1
    ans += d[Asum[l]-K]
print(ans)
