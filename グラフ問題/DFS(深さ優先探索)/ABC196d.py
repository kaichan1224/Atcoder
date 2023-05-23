import io
import sys
sys.setrecursionlimit(10**7)
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
2 2 1 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・深さ優先探索で解けそう

<ポイント>
・3つの置き方をすべてのマスでdfs全探索する→バックトラック忘れないように
・H*W<=16なので3^16で4*10^6で間に合う
・dfsでどのように各マス全探索するかについて
→最後まで探索してy==Hになったら組み合わせ+1
→x==Wまでいったらyを+1する
→使える畳の数が足りなくなったら失敗なのでreturnする
・マスが使われているかどうかはusedで管理する
"""
#--------------------------------------------------------------
H,W,A,B = MAP()
used = [[False]*W for i in range(H)]
cnta = 0 #2*1
cntb = 0 #1*1
ans = 0
def dfs(y,x,a,b):
    global ans
    if a<0 or b<0:
        return
    if x==W:
        x = 0
        y += 1
    if y==H:#このときすべて敷き詰める事ができる
        ans += 1
        return
    if used[y][x]==True:
        return dfs(y,x+1,a,b)
    used[y][x] = True
    dfs(y,x+1,a,b-1)
    if x+1<W and used[y][x+1]==False:
        used[y][x+1] = True
        dfs(y,x+1,a-1,b)
        used[y][x+1] = False
    if y+1<H and used[y+1][x]==False:
        used[y+1][x] = True
        dfs(y,x+1,a-1,b)
        used[y+1][x] = False
    used[y][x]=False
    return ans

print(dfs(0,0,A,B))






