import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
・1->2->...->N->1
・Kがとても大きいから何周+αを考えた方が良さそう
・周期的だからダブリンぐ行ける?
・りんごは全てでK個以上ある

・全てのかごについて、最大何個のりんごを取り出せるかを二分探索する
"""
#-------------------------------
#めぐる式二分探索
def is_ok(arg):
    cnt = 0
    for a in A:
        if a<arg:
            cnt += a
        else:
            cnt += arg
    # 条件を満たすかどうか？問題ごとに定義
    return cnt<=K

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
ans = meguru_bisect(K+1,-1)
eatcnt = 0
for idx,a in enumerate(A):
    if a>=ans:
        A[idx] -= ans
        eatcnt += ans
    else:
        A[idx] = 0
        eatcnt += a
nokori = K-eatcnt
now = 0 #今見ている場所
while nokori>0:
    if A[now]>0:
        A[now] -= 1
        nokori -= 1
    now += 1
    now = now % N
print(*A)
    



