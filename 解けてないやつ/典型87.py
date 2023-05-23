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
<考察>
・i→jまで合計Pスヌーク以下で到達可能な組がちょうどK個
・Xの選び方はいくつか
・各都市は相互移動可能

<ポイント>
f(x):まだ決まっていない辺の長さをすべてxにした場合における最短経路がP以下の頂点対に個数
とすると,f(x)は広義単調減少となる。
f(x)=Kとなるxの個数は
(f(x)<Kとなる最小となる)-(f(x)<=Kとなる最小のx)
"""
#--------------------------------------------------------------
N,P,K = MAP()
A = [LIST() for i in range(N)]






