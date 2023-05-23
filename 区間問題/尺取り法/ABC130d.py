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
10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・尺取で解けそうだけど、要素の和がK以上は普通にやるのは難しそう(K以下なら典型)
→減らす方向で尺取法を考えてみる?

・数えられるパターンからK未満の場合の引けば良い?

<ポイント>
・条件を満たす部分の数え上げはright-left
→right,leftのindexを持つ必要があることに注意

・連続部分列のすべての選び方は(N)+(N-1)+(N-2)+...+1である

<別解>
条件を満たす連続する区間を探すときに左端を全探索して条件を満たす右端を高速に
数え上げれば良区、左端を全探索すると総和がK以上である右端であるかは単調性をもつので
にぶたんで境界線を求めることができる

"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
q = deque()
asum = 0
cnt = 0
right = 0
left = 0
cnt2 = 0
for c in A:
    right += 1
    q.append(c)
    asum += c
    while q and not (asum < K):
        left += 1
        rm = q.popleft()
        asum -= rm
    cnt += right-left
ans = 0
for i in range(N):
    ans += N-i
print(ans-cnt)










