import io
import sys
import sympy as sy
import numpy as np
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""


"""
#-------------------------------
import math
def f(x):
    return 2**(-x**2)

def tyuten(a,b,fx):
    return (b-a)*fx((a+b)/2)

def daikei(a,b,fx):
    return (b-a)*(fx(a)+fx(b))/2

def sinpuson(a,b,fx):
    return 2*tyuten(a,b,fx)/3+daikei(a,b,fx)/3

def gauss(fx,a=-1,b=1):
    return(fx(1/math.sqrt(3))+fx(-1/math.sqrt(3)))

def gauss2():
    z = sy.Symbol('z')
    f = (3*(z+1/math.sqrt(3))/2)**4 # 積分したい関数. 2n-1次以下にする
    n = 2  # 積分点数 (整数値)
    # ルジャンドル多項式のゼロ点x_iと重みw_iを求める
    def leg_weights_roots(n):
        x = sy.Symbol('x')
        roots = sy.Poly(sy.legendre(n, x)).all_roots()  # n次ルジャンドル多項式の根を求める
        x_i = [rt.evalf(20) for rt in roots] 
        w_i = [(2*(1-rt**2)/(n*sy.legendre(n-1, rt))**2).evalf(20) for rt in roots]  # 重み
        return x_i, w_i
    # ガウス求積を実行する
    def gauss_quadrature(f,n):
        xx, ww = leg_weights_roots(n)  # xx:零点のリスト, ww:重みのリスト
        integ = 0
        for i in range(n):
            integ += ww[i]*f.subs(z,xx[i]).evalf()
        return integ
    return gauss_quadrature(f,n)
    
#積分区間,([a,b],f)の順で引数に入れてください
a1 = tyuten(0,2,f)
a2 = daikei(0,2,f)
#a3 = sinpuson(-1,1,f)
#a4 = gauss(f)
#a5 = gauss2()
print(f"中点:{a1}")
print(f"台形:{a2*16}")
#print(f"シンプソン法:{a3}")
#print(f"ガウス積分:{a4}")
#print(f"ガウスむずかしいやつ:{a5}")


