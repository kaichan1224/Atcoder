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
・難易度*気温の総和を最小化したい
・貪欲法はどうか→エスパーしちゃった
・全探索解→N!通り並び方があるから間に合わない

<キーワード>
・貪欲エスパーしちゃいました

<ポイント>


"""
#--------------------------------------------------------------
N = INT()
#難易度
A = LIST()
#気温
B = LIST()
#
A.sort()
B.sort(reverse=True)
ans = 0
for i in range(N):
    ans += A[i]*B[i]
print(ans)

        
