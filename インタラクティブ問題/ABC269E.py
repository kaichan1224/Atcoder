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
"""
<考察>
・二分探索でx,yそれぞれ範囲を絞っていけば良さそう
→あってます!!!!!

<キーワード>
・インタラクティブ問題

<ポイント>
・インタラクティブ問題の時は
def input(): return sys.stdin.readline().strip()
を外せ!!!!!!!!!!!!!!!

・(X,Y)ので答えよの時、座標軸の順番をきちんと見よう!!!!
(y軸,x軸)であることが往々にしてある

"""
#--------------------------------------------------------------
N = INT()
ngx = 0 #C
okx = N+1 #D
ngy = 0 #A
oky = N+1 #B
while (okx-ngx)>1:
    mid = (ngx + okx)//2
    print(f"? {1} {N} {1} {mid}")
    cnt = INT()
    if mid==cnt:#1~midの間になかったら
        ngx = mid
    else:
        okx = mid
        
while (oky-ngy)>1:
    mid = (ngy + oky)//2
    print(f"? {1} {mid} {1} {N}")
    cnt = INT()
    if mid==cnt:#1~midの間になかったら
        ngy = mid
    else:
        oky = mid
print(f"! {oky} {okx}")
        
    
