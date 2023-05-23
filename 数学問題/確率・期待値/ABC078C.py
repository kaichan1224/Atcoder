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
10 2



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
"有効なものが来るまでにカードを引く期待値は、有効なカードを引く確率の逆数"

<問題の見落とし>
・「一度ですべてのケースに正解するまで操作を繰り返す」
→一回目の挑戦でかかる時間を計算して、有効なもの=すべて正解
までに操作する期待値は、全て正解を引く確率の逆数となる
→あとは１つの挑戦でかかる時間の総和＊期待値をすればよい
"""
#--------------------------------------------------------------
N,M = MAP()
time = 1900*M+100*(N-M)
kakuritu = 1/(2**M)
kitaiti = 1/kakuritu
ans = time*kitaiti
print(int(ans))





