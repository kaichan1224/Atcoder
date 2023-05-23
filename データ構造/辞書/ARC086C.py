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
5 2
1 1 2 2 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・辞書のソート
・辞書の最初のキーをindex指定で取り出す方法
"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
cnt = 0
d = defaultdict(int)
for a in A:
    d[a] += 1
d = dict(sorted(d.items(),key=lambda x:x[1]))
syurui = len(d)
while not(syurui<=K):
    cnt += 1
    f = next(iter(d))
    if d[f]==1:
        d.pop(f)
        syurui -= 1
    else:
        d[f] -= 1
if len(d)<=K:
    print(cnt)

        










