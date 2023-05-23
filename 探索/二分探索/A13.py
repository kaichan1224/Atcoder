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
7 10
11 12 16 22 27 28 31
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・小さい順に並んでいるので、
for a,i in enumerate(A):
    差がK以下になるようなa2を2分探索する
    +K(-K)の両方を調べ、そのindex分選べる?
    組合せだから自分より右側の座標だけで良い
    
<キーワード>
・にぶたんor尺取法で解ける
・尺取法で解ける問題がにぶたんで解けることもある！(尺取法の方がより高速ではある)

<ポイント>
・条件を満たす連続的な部分を考えるので尺取法を用いることもできる!!
"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
ans = 0
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    return (A[arg]-a)<=K

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
for i,a in enumerate(A):
    idx = meguru_bisect(N,i)
    ans += idx-i
print(ans)
    
    
    
    
    
