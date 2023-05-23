from cgitb import reset
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
"""
<ポイント>
*データを二次元にプロット
→配列の幅少し大きめにとっておくとバグらせる可能性が低くなる
→文字でおいておくと楽

*二次元累積和
x、y軸方向に累積和をそれぞれとる
ある範囲の個数は包除定理的に考える(余分に引きすぎたところに注意)
s[y~ny][x~nx] = s[ny][nx] - s[ny][x-1] - s[y-1][nx] + s[y-1][x-1]
"""
#--------------------------------------------------------------
N,K = MAP()
m = 5005
plot = [[0]*m for _ in range(m)]
for _ in range(N):
    a,b = MAP()
    plot[a][b] += 1

#x軸方向の累積和
for y in range(m):
    for x in range(m-1):
        plot[y][x+1] += plot[y][x]

#y軸方向の累積和
for x in range(m):
    for y in range(m-1):
        plot[y+1][x] += plot[y][x]

ans = 0
for y in range(1,m):
    for x in range(1,m):
        ny = min(m-1,y+K)#超えないように注意する必要がある
        nx = min(m-1,x+K)
        res = plot[ny][nx] - plot[y-1][nx] - plot[ny][x-1] + plot[y-1][x-1]
        ans = max(ans,res)
print(ans)








