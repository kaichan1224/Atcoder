import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
4 0
1
2
3
4
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
尺取り法をdequeを使って書く
queの中身が何もないときはpopできないので注意
細かいコーナーケースにも気をつける
"""
###################################################
N,K = MAP()
S = [INT() for _ in range(N)]
q = deque()
ans = 0
seki = 1
for c in S:
    if c==0:
        ans = N
    q.append(c)
    seki *= c
    while not (seki<=K) and len(q)>0:
        rm = q.popleft()
        seki = seki//rm
    ans = max(ans,len(q))
print(ans)








