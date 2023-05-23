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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3 3
-1 2
1 1
-2 -3
1
2
3

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
マンハッタン距離→チェビシェフ距離に変換
マンハッタン距離とチェビシェフ距離は一致する
座標の変換は45度回転(x'=x-y,y'=x+y)
(x1,y1),(x2,y2)間のチェビシェフ距離はmax(abs(x1-x2),abs(y1-y2))
"""
######################################################
N,Q = MAP()
X = []
Y = []
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x-y)
    Y.append(x+y)
max_x,min_x,max_y,min_y  = max(X),min(X),max(Y),min(Y)
for _ in range(Q):
    q = INT()
    q -= 1
    ans = max(abs(max_x-X[q]),abs(min_x-X[q]),abs(min_y-Y[q]),abs(max_y-Y[q]))
    print(ans)




