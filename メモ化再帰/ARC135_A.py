import io
import sys
#sys.setrecursionlimit(10**7)
from functools import lru_cache
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
mod = 998244353
######################################################
_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
メモ化再帰の注意点
・再帰が無限に繰り返さないように初期値をきちんと設定する!!
(N==0,1,2,3あたりは要注意)
・lru_cache(10**7)を書いておくと安心
・一応再帰なのでsys.setrecursionlimit(10**7)も忘れず
・答えが大きくなりがちなのでmod忘れないように
"""
######################################################
import sys
sys.setrecursionlimit(10**7)
from functools import lru_cache
mod = 998244353
@lru_cache(maxsize=10**7)
def f(x):
    if x<=4:
        return x
    if x%2==0:
        return f(x//2)*f(x//2)%mod
    else:
        return f(x//2)*f((x-1)//2+1)%mod

X = int(input())
print(f(X)%mod)


