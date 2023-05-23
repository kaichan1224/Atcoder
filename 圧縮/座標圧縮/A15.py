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
5
46 80 11 77 46

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・座標圧縮

<キーワード>

<ポイント>
・座標圧縮のやり方について
setに入れてソートしてから要素が配列の何番目にあるのかを辞書に登録すればよい
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
d = {v:i+1 for i,v in enumerate(sorted(set(A)))}
print(*list(map(lambda v:d[v],A)))