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
4 4
1 2
2 3
3 4
4 1
1 3
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・有向グラフ
・DP的なことしそう
・DAGにしとく?
・始点から3の倍数の地点だったら移動できる

<ポイント>
・拡張BFS:移動先や頂点の情報にさらなる成約がある場合に頂点の情報を追加する
dist[jmp][v]:頂点vにjmp歩目で到達したときの最短距離
・求めたいのはケンケンパの回数なので,最短距離を3で割ったものが答え

"""
#--------------------------------------------------------------
N,M = MAP()
G = [[] for i in range(N)]
for i in range(M):
    u,v = MAP()
    G[u-1].append(v-1)
S,T = MAP()
S,T = S-1,T-1
dist = [[-1]*N for i in range(3)]
dist[0][S] = 1
q = deque()#(v,jmp)
q.append((S,0))
while q:
    now,jmp = q.popleft()
    if now==T and jmp==0:
        print(dist[0][T]//3)
        exit()
    jmp2 = (jmp+1)%3
    for nxt in G[now]:
        if dist[jmp2][nxt]==-1:
            dist[jmp2][nxt] = dist[jmp][now] + 1
            q.append((nxt,jmp2))
print(-1)
        



