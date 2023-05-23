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
4 5 5
1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・ゴールがx,yになるように操作することができるか。
・奇数回目のときx軸方向、偶数回目の時y軸方向に移動することができる
・x,yの座標方面だけ考えれば良い??
というかx,yは対称なのでプラスだけ考えればよさそう

・配るDPを考える

<キーワード>
-10**4-10 ~ 10**4+10の範囲を考えることにする.
(10**4+10)-(-10**4-10)+1=2*10**4+21の大きさ。N番目を反映させていくが、
偶数回と奇数回で分けるので、高々N/2 = 10**3/2

<ポイント>
-10**4~10**4の範囲の大きさの配列サイズは10**8じゃなくて2*10**4+1ですよ???????
"""
#--------------------------------------------------------------
N,gx,gy = MAP()
A = LIST()
xArray = []
yArray = [] 
xcnt = 0
ycnt = 0
for i in range(N):
    if i%2==0:
        xcnt += 1
        xArray.append(A[i])
    else:
        ycnt += 1
        yArray.append(A[i])
sx,sy = 0,0
#dp[i+1個目の移動][移動後の座標]の配るDPを考える
dpx = [[False]*(2*10**4+21) for _ in range(xcnt+1)]
dpy = [[False]*(2*10**4+21) for _ in range(ycnt+1)]
#-10**4+10~10**4+10の範囲を0indexに調整する
t = 10**4+10
dpx[0][sx+t] = True
dpx[1][sx+t+xArray[0]] = True
for i in range(1,xcnt):
    for j in range(2*10**4+21):
        if dpx[i][j]:
            if 0<=j+xArray[i]<2*10**4+21:
                dpx[i+1][j+xArray[i]] = True
            if 0<=j-xArray[i]<2*10**4+21:
                dpx[i+1][j-xArray[i]] = True

dpy[0][sy+t] = True
for i in range(ycnt):
    for j in range(2*10**4+21):
        if dpy[i][j]:
            if 0<=j+yArray[i]<2*10**4+21:
                dpy[i+1][j+yArray[i]] = True
            if 0<=j-yArray[i]<2*10**4+21:
                dpy[i+1][j-yArray[i]] = True

if dpx[xcnt][gx+t] and dpy[ycnt][gy+t]:
    print("Yes")
else:
    print("No")




