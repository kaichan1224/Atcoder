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

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・wl,wr-1が一緒に取り除かれるとき区間[l+1,r-1)はすべて取り除ける
差が1以下のときのみ生じる
・1以外のとき区間[l,i)と区間[i,r)に分けて考える
"""
#--------------------------------------------------------------
def dp(l,r):
    if r-l<=1:
        return 0
    if r-l==2:
        if abs(W[l]-W[l+1])<=1:
            return 2
        else:
            return 0
    



while(True):
    N = INT()
    if N==0:
        break
    W = LIST()






