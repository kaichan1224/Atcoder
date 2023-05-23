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
9
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
*片方固定して考える、上限を考えるはマスト！！
aは最大でも10**6なので全探索で間に合いそう
→あとはbを二分探索で求めるだけ!
"""
######################################################
def f(a,b):
    return a**3+a**2*b+a*b**2+b**3

#めぐる式二分探索
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    return f(a,arg)>=N

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
N = INT()
ans = N
for a in range(0,10**6+1):
    ans = min(ans,f(a,meguru_bisect(0,10**6)))
print(ans)