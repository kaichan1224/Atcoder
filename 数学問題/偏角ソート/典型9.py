import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_left,bisect_right
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
6
245347456 347663468
818348686 227502384
671288933 159695954
557494313 854354542
293850843 607815400
706015854 219870876
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<真ん中決め打ち＋偏角ソート>
・３つある場合、２つ目を固定する

<偏角ソートとは>
・N個の二次元座標上の点が与えられることが多くあり、これらを反時計回りにソートしたい
ときに、反時計回りになるように配列内の順番をソートする

・三角関数はラジアンを受け取って三角形の辺の比を返すので、
逆三角関数の用いれば三角形の辺の比を受け取ってラジアンを知ることができる

・math.atan2(y,x)は引数が２つでarctan(y/x)をラジアンで返す→角度に変換したかったら
math.degrees()をつかう,戻り地は(-pi~pi)

<ポイント>
・角度が大きい点

"""
#--------------------------------------------------------------
N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    X1,Y1 = XY[i]#２つ目を固定する
    dec = []
    #それ以外の点を偏角ソート
    for j in range(N):
        if j==i:
            continue
        X2,Y2 = XY[j]
        x = X2-X1
        y = Y2-Y1
        tmp = math.degrees(math.atan2(y,x))
        if tmp<0:
            tmp = 360+tmp
        dec.append(tmp)
    #偏角ソート
    dec.sort()
    for a in dec:
        c_index = bisect_right(dec,(a+180)%360)
        #indexが範囲外になったときに調整
        c_index = min(c_index,N-2)
        c_index = max(1,c_index)
        c = dec[c_index]
        c2 = dec[c_index-1]
        tmp_degree = min((abs(a-c)),360-abs(a-c))
        tmp_degree2 = min((abs(a-c2),360-abs(a-c2)))
        ans = max(ans,tmp_degree,tmp_degree2)
print('{:.9f}'.format(ans))