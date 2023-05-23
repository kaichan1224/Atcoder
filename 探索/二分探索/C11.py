import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heapify, heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
#def input(): return sys.stdin.readline().strip()　怖いので外します(インタラクティブのとき)
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
1000000 700000 300000 180000


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・こういう問題はまず愚直解を考えるのが重要
・値が最大のものを毎回取り出したい→heapqを使うとよさげ?
→K議席分配のシュミレーションは制約的に無理!
・取り出した政党が何番目の政党なのかの情報が必要!

・視点を変えた2分探索のパターンか?
->K議席分配するときの最小の(票数/議席数の値)を求めることができたら、
それぞれの議席数を求めることができるのでは?

<キーワード>

<ポイント>
・2WAしてしまいました...
→問題分の制約をちゃんと見よう!!!!
-ボーダーとなる「票数÷議席数」の値は1を超え10^9
-ボーターとなる「票数÷議席数」と、次点の「票数÷議席数」の相対誤差は 10^-6

"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
ans = [0]*N
#めぐる式二分探索
def is_ok(arg):
    cnt = 0
    for a in A:
        cnt += a//arg
    return cnt<=K

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng)>10**(-6)):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

hirei = meguru_bisect(1,10**9)
for i,a in enumerate(A):
    ans[i] = int(a//hirei)
print(*ans)

    

