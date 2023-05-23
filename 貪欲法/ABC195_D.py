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
3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
l,l+1,..rの箱以外の箱に入れることが出来る価値の合計の最大化
解法1:貪欲,容量が小さい箱から順番に、価値が大きい荷物を入れる
解法2:貪欲エスパーが難しい場合、最小費用流
"""
######################################################
N,M,Q = MAP()
WV = [LIST() for _ in range(N)]
WV.sort(reverse=True,key=lambda x:x[1])
X = LIST()
ans = 0
for _ in range(Q):
    l,r = MAP()
    l,r = l-1,r-1
    now = X[0:l]+X[r+1:]
    cnt = 0
    now.sort()
    used = [False]*N
    for n in now:#箱が小さい順に埋めていく
        for i in range(N):#価値が最大のものを
            if n>=WV[i][0] and used[i]==False:
                used[i]=True
                cnt += WV[i][1]
                break
    print(cnt)














