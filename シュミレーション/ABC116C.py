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
8
4 23 75 0 23 96 50 100




"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・シュミレーション問題?(実装重め)

<ポイント>
・操作どおりに実装したが、すべての高さが0になるまで減らすのもあり
・区間ごとに切り出す処理をどうやってやるか
・一番低い値と比べて...とかやらなくても高さごとに分割する要素が何個あるかを見ていけば良い

<区間ごとに切り出す処理>
0,0,1,1,1,0,1,1,1 1が連続する部分が何箇所あるか
(コード)

idx = 0
cnt = 0
while idx<N:
    if h[i]==0:
        i += 1
    else:
        cnt += 1
        while idx<N and h[idx]>0:
            idx += 1

"""
#--------------------------------------------------------------
N = int(input())
h = LIST()
now = [0]*N
cnt = 0
if min(h)!=0:
    cnt += min(h)
    now = [min(h)]*N
else:
    now = [0]*N
nowmin = min(now)
for k in range(max(h)):
    l = 0
    r = 0
    for i in range(N):
        if h[i]==now[i]:
            flag = True
            for j in range(l,r):
                now[j] += 1
            if l!=r:
                cnt += 1    
            l = i+1
            r = i+1
        else:
            flag = False
            r += 1
        if flag==False and i==N-1:
            for j in range(l,r):
                now[j] += 1
            cnt += 1
print(cnt)


    




