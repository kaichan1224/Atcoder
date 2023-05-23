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
5 2
1 100
1 1000000000
101 1000
9982 44353
1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
貪欲法、区間スケジューリングの応用問題
今回の一番の肝は、壁の右端が短い順に並べ右側にパンチをうつこと
が最適解であるということ

気づきまとめる→考察→実装のステップが重要
"""
######################################################
N,D = MAP()
LR = []
for _ in range(N):
    l,r = MAP()
    LR.append((l,r))
LR.sort(key=lambda x:x[1])
print(LR)
cnt = 0
i = 0
while(True):
    if i==N:
        break
    t = LR[i][1]
    cnt += 1
    while(True):
        i += 1
        if i==N:
            break
        if t+D-1<LR[i][0]:
            break
print(cnt)


