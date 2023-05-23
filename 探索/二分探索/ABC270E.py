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
2 1000000000000
1000000000000 1000000000000


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・何周すると全部のコマがなくなるかギリギリの範囲を調べる
→2分探索
<キーワード>

<ポイント>
・あってます
・条件部分の細かいミス、細かい実装ミスがありました(実装力不足)
"""
#--------------------------------------------------------------
#めぐる式二分探索
def is_ok(arg):
    flag = True
    num = 0
    for i in range(N):
        if A[i]-arg>=0:
            num += arg
        else:
            num += A[i]
    return num<K
        
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
N,K = MAP()
A = LIST()
sumA = sum(A)
tmp = meguru_bisect(10**12+1,-1)
num = 0
for i in range(N):
    if A[i]-tmp>=0:
        num += tmp
    else:
        num += A[i]
for i in range(N):
    if A[i]-tmp>=0:
        A[i] -= tmp
    else:
        A[i] = 0
cnt = K - num
i = 0
while cnt>0:
    if A[i]>0:
        A[i] -= 1 
        cnt -= 1
    i += 1
print(*A)
    

