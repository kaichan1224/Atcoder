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
・左をL,右側のRで置き換えていった時にAの要素の総和として考えられる最小値
・ポイント：数式を立てて機械的に解く、求めたいものを立式する

今回の問題はa0,..,ax-1,ax,..,ay-1,ay,...,aN-1であり、
求めたいのは0<=x<=y<=Nの時の
min(L*x+cum[y]-cum[x]+R*(N-y))
順番に左からx個だけLで置き換えたもの、連続部分区間なのでただの累積和の差、右からN-y個だけRで置き換えたもの
である。

この時、中身を式変形する。今回の問題はO(N)なら解けるのでxを全探索する方針を考えると、
min(L*x-cum[x]+R*N)+min(cum[y]-R*y)と分解でき、min(cum[y]-R*y)が分かっていれば解ける
ここで、min(cum[y]-R*y)はx<=y<=Nであるが、事前に計算できる?

<わかりやすい考え>
・当時嘘解法として、元からどれだけ小さくできたかを考えていた
・左側の最小と右側の最小を組み合わせれば良い。
"""
#--------------------------------------------------------------
N,L,R = MAP()
A = LIST()
cumA = [0]
for i in range(N):
    cumA.append(min(cumA[i]+A[i],L*(i+1)))
cumB = [0]
for i in range(N):
    cumB.append(min(cumB[i]+A[N-1-i],R*(i+1)))
ans = INF
#print(cumA,list(reversed(cumB)))
for i in range(N+1):
    ans = min(ans,cumA[i]+cumB[N-i])
print(ans)


    
