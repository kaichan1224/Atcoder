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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3 5
...#.
.#.#.
.#...
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
考察
木ではないが直径を求める問題に似ている
→適当な点から幅優先探索し、もっとも距離が遠いところからBFS
→ただし連結成分数が複数ある場合、求められていない部分があるので
全ての.マスでBFS


"""
######################################################
H,W = MAP()
grid = [list(input()) for _ in range(H)]

ans = 0
for y in range(H):
    for x in range(W):
        if grid[y][x]=='.':
            sh,sw = y,x           
            que = deque()
            que.append((sh,sw))
            dist = [[-1]*W for _ in range(H)]
            dist[sh][sw] = 0
            while que:
                h,w = que.popleft()
                for dy,dx in dirc:
                    nh,nw = h+dy,w+dx
                    if not(0<=nh<H and 0<=nw<W):
                        continue
                    if dist[nh][nw]==-1 and grid[nh][nw]=='.':
                        dist[nh][nw] = dist[h][w] + 1
                        que.append((nh,nw))
            distmax = 0            
            for h in range(H):
                for w in range(W):
                    if distmax<dist[h][w]:
                        distmax = dist[h][w]
                        gh,gw = h,w

            que = deque()
            que.append((gh,gw))
            dist = [[-1]*W for _ in range(H)]
            dist[gh][gw] = 0
            while que:
                h,w = que.popleft()
                for dy,dx in dirc:
                    nh,nw = h+dy,w+dx
                    if not(0<=nh<H and 0<=nw<W):
                        continue
                    if dist[nh][nw]==-1 and grid[nh][nw]=='.':
                        dist[nh][nw] = dist[h][w] + 1
                        que.append((nh,nw))

            distmax = 0            
            for h in range(H):
                for w in range(W):
                    if distmax<dist[h][w]:
                        distmax = dist[h][w]
            ans = max(ans,distmax)
print(ans)

        

