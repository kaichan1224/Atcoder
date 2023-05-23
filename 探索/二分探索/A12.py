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
4 10
1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・制約から答えが10**9を超えないことがわかっている
→答えで二分探索

・答えで二分探索をするなら、arg秒時点で何枚のチラシが印刷されるかを求める必要がある
・答えcntが==KだったらTrue,そうでなければFalseを返す
・各プリンターarg秒//aの商が印刷できるチラシの枚数となり、これはO(N)で求めることができる

<キーワード>
・答えで二分探索

<ポイント>
・解くの遅すぎ
・答えでにぶたんが使える条件は、答えがx以上かという質問に答えられる場合に利用することができる
・単調増加、単調減少の時とかetc
"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    cnt = 0
    for a in A:
        cnt += arg//a
    return K<=cnt

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
print(meguru_bisect(-1,10**9+1))
