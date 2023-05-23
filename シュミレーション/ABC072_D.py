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
9
1 2 4 9 5 8 7 3 6
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
*入れ替えるのは隣り合う２つであることに注意
*貪欲？にindex小さい順に入れ替え、違う部分の距離だけans +=した→4WA
*距離が近い部分から入れ替えたほうがよい
*偶数個あるときは//2個入れ替えれば良い
*間の個数は-1,

<解説>
シュミレーションするだけ。。。
"""
#--------------------------------------------------------------
N = INT()
P = LIST()
cnt = 0
for i in range(N):
    print(P)
    if P[i]==i+1:
        if P[i] == i+1:
            if P[i]==N:
                P[i-1],P[i] = P[i],P[i-1]
            else:
                P[i],P[i+1] = P[i+1],P[i]
            cnt += 1
print(cnt)











