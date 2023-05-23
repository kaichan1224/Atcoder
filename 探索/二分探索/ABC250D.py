from bisect import bisect_right
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
250
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
素数列挙と二分探索
・条件を満たす最大のindexをとりたい→めぐる式使いましょう
・p<qの条件を見落とさないようにしましょう→q-p>0ならansに加算
めぐる式イズ最強
"""
#--------------------------------------------------------------
def is_ok(idx):
    qd = iq[idx]
    return qd*qd*qd*i<=N 

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

def Eratosthenes(N):
    # テーブル
    isprime = [True] * (N+1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか
    return isprime

# 50 以下の素数をすべて求める
N = INT()
T = int(math.pow(N,1/3))
p = Eratosthenes(T)
q = Eratosthenes(T)
ip = [i for i,x in enumerate(p) if x==True]
iq = [i for i,x in enumerate(q) if x==True]
ans = 0
for idx,i in enumerate(ip):
    tmp = meguru_bisect(len(iq),-1)-idx
    if tmp<0:
        tmp = 0
    ans += tmp
print(ans)




