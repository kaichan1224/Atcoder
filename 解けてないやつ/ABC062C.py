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
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
H*Wのチョコをできるだけ3等分したい時の、最大面積と最小面積の差
→mod3で解ける?
→全然だめ
→3つのピースは長方形でなければならない


・H,Wのどちらかが3の倍数ならば、縦横どちらかに3等分すればよくその時の答えは0
・実装めんどくさい
→分け方を場合分けして実装すればいい!!

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
H,W = MAP()
print(H*W%3)