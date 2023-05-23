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
10 12
9 1
#.^<..><<...
#<>.#<^.<<.^
^.<>.^.^.^>.
^.>#^><#....
.>.^>#...<<>
....^^.#<.<.
.>^..^#><#.^
......#>....
..<#<...^>^.
<..^>^^...^<

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
グラフを逆向きに貼って考える
マス(a,b)からマス(r,c)に動かせるか全てのマスでbfs→TLE
グラフの全ての辺を逆向きにして(r,c)からBFSでたどり着けるか判定
すればO(HW)で解ける
<注意>
グラフの向きを逆向き→移動先のマスの状態で移動方向を決める必要がある
"""
######################################################
H,W = MAP()
r,c = MAP()
r,c = r-1,c-1
grid = [list(input()) for _ in range(H)]
ans = [['']*W for _ in range(H)]
dist = [[False]*W for _ in range(H)]
dist[r][c]=True
que = deque()
que.append((r,c))
while que:
    y,x = que.popleft()
    if grid[y][x]=='.':
        for dy,dx in dirc:
            ny,nx = y+dy,x+dx
            if not (0<=ny<H and 0<=nx<W):
                continue
            if dist[ny][nx]==False and grid[ny][nx]!='#':
                que.append((ny,nx))
                dist[ny][nx]=True
    elif grid[y][x]=='^':
        ny,nx = y+1,x
        if not (0<=ny<H and 0<=nx<W):
            continue
        if dist[ny][nx]==False and grid[ny][nx]!='#':
            que.append((ny,nx))
            dist[ny][nx]=True
    elif grid[y][x]=='>':
        ny,nx = y,x-1
        if not (0<=ny<H and 0<=nx<W):
            continue
        if dist[ny][nx]==False and grid[ny][nx]!='#':
            que.append((ny,nx))
            dist[ny][nx]=True
    elif grid[y][x]=='<':
        ny,nx = y,x+1
        if not (0<=ny<H and 0<=nx<W):
            continue
        if dist[ny][nx]==False and grid[ny][nx]!='#':
            que.append((ny,nx))
            dist[ny][nx]=True
    elif grid[y][x]=='v':
        ny,nx = y-1,x
        if not (0<=ny<H and 0<=nx<W):
            continue
        if dist[ny][nx]==False and grid[ny][nx]!='#':
            que.append((ny,nx))
            dist[ny][nx]=True

print(dist)
for h in range(H):
    for w in range(W):
        if grid[h][w]=='#':
            ans[h][w] = '#'
        elif dist[h][w]:
            ans[h][w] = 'o'
        else:
            ans[h][w] = 'x'

for h in range(H):
    for w in range(W):
        print(ans[h][w],end='')
    print()


########
#解答例#
########
"""
from collections import deque
h, w = map(int, input().split())
r, c = map(int, input().split())
r -=1
c -=1
G =[]
A =[]
d = [(-1,0),(0,1),(1,0),(0,-1)]
T = [["x"] *w for _ in range(h)]
for i in range(h):
  s = input()
  for j in range(w):
    if s[j] =="#":
      T[i][j] ="#"
  G.append(s)
    
visited = [[False]*w for _ in range(h)]


q =deque()
q.append((r,c))
visited[r][c]=True
while q:
  x,y = q.popleft()
  T[x][y] ="o"
  if y+1<w and visited[x][y+1] ==False:
    if G[x][y+1]=="." or G[x][y+1] =="<":
      visited[x][y+1] =True
      q.append((x,y+1))
  if y-1>=0 and visited[x][y-1] ==False:
    if G[x][y-1]=="." or G[x][y-1] ==">":
      visited[x][y-1] =True
      q.append((x,y-1))
  if x+1<h and visited[x+1][y] ==False:
    if G[x+1][y] =="." or G[x+1][y] =="^":
      visited[x+1][y] = True
      q.append((x+1,y))
  if x-1>=0 and visited[x-1][y] ==False:
    if G[x-1][y] =="." or G[x-1][y] =="v":
      visited[x-1][y] = True
      q.append((x-1,y))
      
for i in range(h):
  print(''.join(T[i]))    
"""




