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
・ナップサックが一つだけだったら
dp[i][A]:i個目の段階で重さがAの時の価値で求めることができる
・ナップサックが二つの時を考えると
dp[i][A][B]:i個目の段階で一つ目のナップサックがA以下,二つ目のナップサックがb以下

<キーワード>

<ポイント>

"""
#--------------------------------------------------------------
N,A,B = MAP()



        
        