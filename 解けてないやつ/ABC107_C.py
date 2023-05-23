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
3 3
1 2 2
2 3 3
1 3 6

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
* 貪欲に考える
* 0から絶対値を取って、小さい順に並べる。
* なるべく同じ方向が良い
* 一旦行く方向を決めて、前後の距離が近い方に移動する?
<point>
* 移動する方向を決めて、端までついたら逆向きに移動する


"""
#--------------------------------------------------------------
N,K = MAP()
x = LIST()





