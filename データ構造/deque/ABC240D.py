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
<ポイント>
・データの持ち方を工夫する
・スタックをうまく使う

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
q = [[A[0],1]]
cnt = 1
print(cnt)
for a in A[1:]:
    if len(q)!=0 and a==q[-1][0] and  a!=q[-1][1]+1:
        q[-1][1] += 1
        cnt += 1
    elif len(q)!=0 and a==q[-1][0] and a==q[-1][1]+1:
        q.pop()
        cnt -= (a-1)
    elif len(q)!=0 and a!=q[-1][0]:
        q.append([a,1])
        cnt += 1
    else:
        q.append([a,1])
        cnt += 1
    print(cnt)
    
    
    
    
