import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate

from numpy import append
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
4 3
4 3
9 5
15 8
8 6
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
貪欲法(コツはまず貪欲で試してみること!)
貪欲法で行けるのかどうかの部分が一番難しい（エスパー的）
→貪欲で行けるのか不安なときはとりあえずいくつかのコーナーケース
で試してみるのが一番

今回の問題はB[i]>A[i]-B[i]が保証されているため、
n-1回目までにその問題の部分点が取られているので選べる
"""
######################################################
N,K = MAP()
AB = [LIST() for _ in range(N)]
score = []
for i in range(N):
    score.append(AB[i][1])
    score.append(AB[i][0]-AB[i][1])
score.sort(reverse=True)
print(sum(score[:K]))



