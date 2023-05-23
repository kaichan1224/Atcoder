import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left
from traceback import print_tb 
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
10000000000 10 99959
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・一旦愚直にやってみて法則性があるかまずはみてみる
・周期性があるタイプ
・一回0になったら打ち切って良い
・Mは高々10**5なので、周期を見つける段階で制約が超えることはない

<キーワード>
・法則見つけて実装するだけ

<ポイント>
・実装下手すぎませんか?
・時間かけてACjapan!

"""
#--------------------------------------------------------------
N,X,M = MAP()
def f(x,m):
    return x%m
a = [0]*(10**5+10)
a[0] = 0
a[1] = X
numset = {a[1]}
idx = None
for i in range(1,N):
    a[i+1] = f(a[i]**2,M)
    if a[i+1] == 0:
        break
    if a[i+1] in numset:
        idx = i+1
        break
    numset.add(a[i+1])
if idx==None:
    print(sum(a))
    exit()

b = a.index(a[idx])
ans = 0
for i in range(1,b):
    ans += a[i]
roopsum = 0
for i in range(b,idx):
    roopsum += a[i]
roop = idx-b
#ループする個数
N2 = N-b+1
q,r = divmod(N2,roop)
ans += q*roopsum
for i in range(b,b+r):
    ans += a[i]
print(ans)




    
