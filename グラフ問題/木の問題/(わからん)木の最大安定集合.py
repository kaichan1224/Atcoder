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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
10
4 6
3 1
2 4
5 6
6 9
0 4
7 3
6 8
4 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・木の最大安定集合
安定集合：どの2頂点も辺で結ばれていないようなもの
→葉から考えていく考察によってうまくいく


・制約を見よう：与えられるグラフは木である

"""
#--------------------------------------------------------------
N = INT()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    G[a].append(b)
    G[b].append(a)
    
color = [-1]*N
color[0] = 0
que = deque([0])
while que:
    now = que.popleft()
    for nxt in G[now]:
        if color[nxt]==-1:
            que.append(nxt)
            color[nxt] = 1 if color[now]==0 else 0
            
white = 0
black = 0
print(color)
for a in color:
    if a==0:
        white += 1
    else:
        black += 1
print(max(white,black))
