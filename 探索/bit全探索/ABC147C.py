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
3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
Nが15と小さい→bit全探索
i番目の人が正直者か、不親切な人かを全探索する
最大何人の正直者が存在し得るか→矛盾が生じない最大の人数

矛盾が生じたらだめ→正直だと仮定した人の証言が間違っていたらflase
"""
#--------------------------------------------------------------
N = INT()
XY = []
for i in range(N):
    a = INT()
    xy = [LIST() for i in range(a)]
    XY.append(xy)
ans = 0
for bits in product([0,1],repeat=N):#正直者だと仮定する
    is_ok = True
    cnt = 0
    for i in range(N):
        if bits[i]==0:#不親切な人
            continue
        cnt += 1
        for a,b in XY[i]:
            if bits[a-1]!=b:
                is_ok = False
    if is_ok:
        ans = max(ans,cnt)
print(ans)








