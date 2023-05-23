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
#---------------------------------------------------------------
_INPUT = """\
5 3
6 11 2 5 5
5
20
0


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・区間和の総和求めるだけなら累積和で余裕で可能(なんでできないアホ?)
・区間の更新が入るとセグメント木が必要
・2分探索バグらせ過ぎでは?
"""
#--------------------------------------------------------------
N,Q = MAP()
A = LIST()
A.sort()
Asum = list(accumulate(A))
def is_ok(arg):
    #条件を満たす最大を求めたい
    return A[arg]<=X

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
for _ in range(Q):
    X = INT()
    idx = meguru_bisect(ng=N,ok=-1)
    if idx==-1:
        print(Asum[N-1]-X*N)
    elif idx==N-1:
        print(X*N-Asum[N-1])
    else:
        tmp = 0
        tmp += X*(idx+1)-Asum[idx]
        tmp += Asum[N-1]-Asum[idx]-(X*(N-(idx+1)))
        print(tmp)



