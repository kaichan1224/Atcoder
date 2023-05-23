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
3.0000
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
T(334)
→x=0年のときはP年かかる
→x年後のときは速度は2^(x/1.5)つまり、x/(2^(x/1.5))かかる
t年時点での、計算が終わるまでの時間はf(t)=t+P/(2**(t/1.5))

<ポイント>
三分探索:たかだか1つしか極地のない関数fにおける極地を探索するアルゴリズム

アルゴリズム:
highとlowの間を三分割させ、mid_left,mid_rightを設ける
この2点についてf()が大きい方(極大の場合は小さい方)にhigh/lowを寄せるのを繰り返す
"""
#--------------------------------------------------------------
def f(x):#t年後
    return -1*(x**2)

P = float(input())

left = -10000
right = 10000

def totu_search(low,high):
    while high - low >1e-9:#誤差
        mid_left = high/3+low*2/3
        mid_right = high*2/3+low/3
        if f(mid_left) <= f(mid_right):
            low = mid_left
        else:
            high = mid_right
    ans = low
    return ans

#その時のf(t)の値←今回求めるのはこっち
print(f(totu_search(left,right)))





