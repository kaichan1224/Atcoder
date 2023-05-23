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
2 7 1 8 2
3 1 4 1 5

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・1回操作をするたびにaの数列の総和がbの総和に比べて1づつ増える
・aiに2を足す、bjに1を足すという操作を同時に何回でも行える
・貪欲にやる
・基本aiの方が総和が増える速度が早いので、aiがbiに合わせるスタイル?

<解説>
・aの方が全体的に小さい必要がある
→a[i]>b[i]のところについて、b[i]に1足す代わりに、a[j]<b[j]のところにa[j]に2足す

・成約はちゃんと見よう N=10^4なので二重ループでも間に合います。
・
"""
#--------------------------------------------------------------
N = int(input())
a = LIST()
b = LIST()
biggerA = 0
biggerB = 0
for i in range(N):
    if a[i]>b[i]:
        biggerA += a[i]-b[i]
    if b[i]>a[i]:
        biggerB += (b[i]-a[i])//2
if biggerB>=biggerA:
    print("Yes")
else:
    print("No")








