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
"""
<考察>
・合計Xステージクリアするのにかかる時間の最小値
・X<=10**9よりX回調べることはできない
・2回目以降はBのみでクリアできる
・スキップするのは一個だけで良い?
→今までのプレイ回数をmとするとX-m回だけ掛ければ求めることができるのでは
"""
#--------------------------------------------------------------
N,X = MAP()
AB = [LIST() for _ in range(N)]
ans = INF
tmp = 0
for i in range(min(N,X)):
    tmp += AB[i][1]+AB[i][0]
    ans = min(ans,tmp+AB[i][1]*(X-(i+1)))
print(ans)