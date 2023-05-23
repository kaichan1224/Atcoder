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
_INPUT = """\
5 3
1 2
2 3
3 4


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・すべての人と知り合い→unionfindではない
・Nが小さい→bit全探索

<注意>
・pypyだとMLE:メモリ制限超過した
・pypyは早いけどメモリ使用量が多いので注意
"""
#--------------------------------------------------------------
N,M = MAP()
G = [[False]*N for i in range(N)]
for i in range(N):
    G[i][i] = True
for i in range(M):
    x,y = MAP()
    x,y = x-1,y-1
    G[x][y] = True
    G[y][x] = True
ans = 0
for bits in product([0,1],repeat=N):
    comb = [i for i,x in enumerate(bits) if x==1]
    cnt = len(comb)
    flag = True
    for i in comb:
        for j in comb:
            if G[i][j]==False:
                flag = False
    if flag:
        ans = max(ans,cnt)
print(ans)

            






