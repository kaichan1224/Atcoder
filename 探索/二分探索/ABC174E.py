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
10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202





"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・最も長い丸太の長さが最小でいくつになるか→最大値の最小化→２分探索
・答えを決め打つタイプのやつ
・長い部分だけ情報を持つ

<ポイント>
・切る必要がある回数をis_okで判断する
・長さMの丸太をL以下にする切断数はfloor((M-1)/L)で計算できる←なんで?
→floot(a/x)-1
"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
def is_ok(arg):
    logs = 0
    for a in A:
        logs +=math.floor((a-1)/arg)
        #logs +=math.ceil(a/arg)
    return logs<=K

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
#長さで二部探索
ans = meguru_bisect(ng=-1,ok=10**9)
print(ans)





