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


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
２分探索できるように配列をつくる
"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
swap_list = []
now = 0
# K番目(0-indexなので実質K+1番目)以降のもののうち、
# 入れ替えたら得点があがりうるもののリスト

#重要ポイント
# (入れかることができるリストを昇順で管理できるようにすることで)
#２分探索できるようにしている(小さい部分はむ)
for i in range(K,N):
    now = max(now,A[i])
    swap_list.append(now)

ans = 10**18
for i in range(K):
    #k番目以内でA[i]より大きいもののswap_listのindex
    idx = bisect_right(swap_list,A[i])
    if idx<len(swap_list):
        #移動回数はK番目＋(ずらした部分)-iで求めることができる
        ans = min(ans,K+idx-i)
if ans==10**18:
    print(-1)
else:
    print(ans)





