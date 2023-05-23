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
2 2021
2 3
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
答えで決め打つ二分探索
ある値Xが与えられたとき、〇〇を満たすことはできるか」という判定問題を考え、
その判定問題を繰り返す解くことでYesになるXとNoになるXの間の境界を特定し、
元の問題の答えを求める

解法1:各操作時に楽しさが最大のアトラクションを選ぶことを繰り返す
        地道に-1するとTLEしてしまうので次に大きい数と一致するまで
        一気に減らす工夫をすると高速化できる
解法2:楽しさがm以上のアトラクションにすべて乗ったとき、
        乗った回数がK回以下になるかをニブタンする
"""
######################################################
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    cnt = 0
    for x in A:
        if x>=arg:#それぞれの乗り物についてarg以上のものの個数をカウントする
            cnt += x-arg+1
    return cnt<=K #楽しさarg以上の乗った回数の合計回数がK以下のとき条件を満たす

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
m = meguru_bisect(ng=0,ok=2*10**9+1)
rem = K
ans = 0
#M以上の要素を全て選ぶ(等差数列の和の公式を用いてansに加算)
for i in range(N):
    x = A[i]
    if x>=m:
        diff = x-m+1
        ans += diff*(x+m)//2
        rem -= diff
#残りK個に満たない部分はM-1を残り回数分選ぶ
ans += rem*(m-1)
print(ans)
