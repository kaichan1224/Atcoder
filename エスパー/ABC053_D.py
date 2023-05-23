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
15
1 3 5 2 1 3 2 8 8 6 2 6 11 1 1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
すべて異なるように取り出す
三枚抜き出し、最大、最小を選び、残りをカードの山に戻す
被っているものを取り出す
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
n = len(set(A))
if n%2==1:
    print(n)
else:
    print(n-1)







