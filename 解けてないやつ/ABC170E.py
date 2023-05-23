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
・操作C→Dに所属を移動
・求めたいのはすべての幼稚園のうち、最もレートが高いものの最小値

<ポイント>
・各幼稚園について最高レートのみ管理すれば良い
"""
#--------------------------------------------------------------
N,Q = MAP()
AB = [LIST() for i in range(N)]
for i in range(Q):
    c,d = MAP()







