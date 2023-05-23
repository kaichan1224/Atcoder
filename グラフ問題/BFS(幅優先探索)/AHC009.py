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
import random
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
1 2 19 16 0.10
0010000100110011100
1000001000001000001
0000000000000000010
0100000000000110100
0000000000000000100
1000101100000101010
0010001011000110000
0000001001000000000
0000000100010001001
0010010000100000001
0001000010000100000
0011010000000001000
0000000101010100000
0000001000000100010
0110100010000000000
0010011101000101000
0000100110010000000
0010000101101000010
1001000000000000000
1000110000000000000
00000001000000000100
00001000010001000000
00010001010000010000
01110010101000010100
00000000000001100000
00001000010000000100
00101000000010110011
01010100000000000000
00001101010010010010
10000000000000010100
01011010000001100100
00000000000000010011
00001100111000110100
00000010000000000000
00010000100111000000
11010000001001010100
01100010011001011001
00000101000010101010
00100000000000000001
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
迷路（壁情報が与えられたver）における経路復元
壁情報の扱いに要注意！
幅優先探索の経路復元は直前の移動方向をx,yそれぞれ記憶する
"""
######################################################
si,sj,ti,tj,p = map(float,input().split())
si,sj,ti,tj = int(si),int(sj),int(ti),int(tj)
h = [input() for _ in range(20)]
v = [input() for _ in range(19)]

ans = ''
dist = [[-1]*20 for  _ in range(20)]
dist[si][sj]=0
q = deque()
q.append((si,sj))
prev_x = [[-1]*20 for _ in range(20)]
prev_y = [[-1]*20 for _ in range(20)]
while q:
    y,x = q.popleft()
    for dx,dy in dirc:
        ny,nx = y+dy,x+dx
        if 0<=ny<20 and 0<=nx<19:
            if h[ny][nx-1]=='1' and dx==1 and dy==0:
                continue
        if 0<=ny<20 and 0<nx<19:
            if h[ny][nx]=='1' and dx==-1 and dy==0:
                continue
        if 0<=ny<19 and 0<=nx<20:
            if v[ny][nx]=='1' and dx==0 and dy==-1:
                continue
        if 0<ny<19 and 0<=nx<20:
            if v[ny-1][nx]=='1' and dx==0 and dy==1:
                continue
        if not (0<=ny<20 and 0<=nx<20):
            continue
        if dist[ny][nx]==-1:    
            q.append((ny,nx))
            dist[ny][nx] = dist[y][x] + 1
            #直前のx方向、y方向の移動場所を記録しておく
            prev_x[ny][nx] = x
            prev_y[ny][nx] = y
score = dist[tj][ti]
x = tj
y = ti
field = [['.']*20 for _ in range(20)]
while x!=-1 and y!=-1:
    field[y][x]='o'
    px = prev_x[y][x]
    py = prev_y[y][x]
    x = px
    y = py

tmp = ''
que = deque()
que.append((si,sj))
dist = [[False]*20 for _ in range(20)]
dist[si][sj]=True
while que:
    y,x = que.popleft()
    for dx,dy in dirc:
        ny,nx = y+dy,x+dx
        if 0<=ny<20 and 0<=nx<20 and field[ny][nx]=='o' and dist[ny][nx]==False:
            dist[ny][nx]=True
            que.append((ny,nx))
            if (dx,dy)==(1,0):
                tmp += 'R'
            elif (dx,dy)==(-1,0):
                tmp += 'L'
            elif (dx,dy)==(0,1):
                tmp += 'D'
            else:
                tmp += 'U'

#print(tmp)

alp = 'RLDU'
ans = ''
for i in range(len(tmp)):
    ans += tmp
    if random.randint(0,100)<int(p*100):
        ans += 'D'
        ans += 'L'
ans = ans[:50]
print(ans)
#経路復元
for i in range(20):
    for j in range(20):
        print(field[i][j],end='')
    print()
