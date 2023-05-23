import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
9 11
4 9
9 1
8 2
8 3
9 2
8 4
6 7
4 6
7 5
4 5
7 8
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
既に二部グラフでない場合はどうしようもない.
主客転倒テク使う???
余事象?? ->余事象です!!!!!!

<ポイント>
・グラフ全体が二部グラフとなるかがポイント
→みている部分ではない!!!

○前提として、現時点で全てのグラフが二部グラフである必要がある
・グラフが全て連結の場合
->N/(N-1)-(同じ色のペアの個数)-(直接つながっている辺の数=総数M)

・グラフが非連結の場合
->非連結のグラフ同士は必ず二部グラフになる(0,1の順番を反転させればいいだけだから)

"""
#-------------------------------
N,M = MAP()
G = [[] for _ in range(N)]

for _ in range(M):
    u,v = MAP()
    u,v = u-1,v-1
    G[u].append(v)
    G[v].append(u)
ans = N*(N-1)//2-M
flag = True
color = [-1]*N
for n in range(N):
    if color[n]==-1:
        que = deque()
        que.append(n)
        color[n] = 0
        red = 0
        blue = 0
        red += 1
        while que:
            now = que.popleft()
            for nxt in G[now]:
                if color[nxt]==-1:
                    color[nxt] = 1-color[now]
                    if color[nxt]==0:
                        red += 1
                    else:
                        blue+= 1
                    que.append(nxt)
                if color[now]==color[nxt]:
                        flag = False
        ans -= red*(red-1)//2
        ans -= blue*(blue-1)//2
if flag:
    print(ans)
else:
    print(0)









