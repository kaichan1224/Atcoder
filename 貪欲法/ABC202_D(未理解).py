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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
2 2 4

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
辞書順最小は前から貪欲(前から決めていく)
*次の文字に置けるものとして最も早い文字chを貪欲に付け足すことを
繰り返すと辞書順最小がもとまる
"""
######################################################
from math import comb
A,B,K = MAP()
a = A #残っているAの数
b = B #残っているBの数
ans = ''

while a>0 and b>0:
    #i文字目がaの文字列は(a-1+b)C(a-1)種類あり、
    #i文字目がbの文字列は辞書順で最も早くて(a-1+b)C(a-1)+1番目
    #つまり、K<(a-1+b)C(a-1)であれば,i文字目はa,そうでなければbとなる
    a_comb = comb(a-1+b,a-1)
    if K <= a_comb:#2文字目も同様にa,b判定する
        ans += "a"
        a -= 1 
    else:
        ans += "b"
        b -= 1
        K -= a_comb#一文字目がaの文字列だけKをへらす
ans += "a" * a
ans += "b" * b
print(ans)