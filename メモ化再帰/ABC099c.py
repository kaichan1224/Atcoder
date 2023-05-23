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
#メモ化再帰 from functools import lru_cache
#@lru_cache(maxsize=1000)
INF = float('inf')
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
127

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
N = 10**5だから何かしらの全探索またはdfsで工夫すれば解けそう?

<ポイント>
・メモ化再帰(DP)
・トップダウンにNを降下する(メモ化再帰しないと大変なことになるので注意!)
1円払った場合にはf(N-1)+1枚かかる、6円払った場合にはf(N-6)+1円かかる
というように場合分けしてこれらの最小値を取る
・貪欲に高い硬化から払っていくのが良さそうに見えるが、だめな例がある
"""
#--------------------------------------------------------------
from functools import lru_cache

N = INT()
@lru_cache(maxsize=1000)
def f(v):#f(n):n円引き出すのに必要最小の操作回数
    if v==0:
        return 0
    res = float('inf')
    #1円
    res = min(res,f(v-1)+1)
    #6円
    x = 6
    while (x<=v):
        res = min(res,f(v-x)+1)
        x *= 6
    #9円
    x = 9
    while (x<=v):
        res = min(res,f(v-x)+1)
        x *= 9
    return res

print(f(N))





