import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
#-------------------------------
"""
なもりグラフ
両方とも閉路の中にあったら2、それ以外なら1
"""
#-------------------------------
N = INT()
G = [[] for _ in range(N)]
outnum = [0]*N
for _ in range(N):
    u,v = MAP()
    u,v = u-1,v-1
    G[u].append(v)
    G[v].append(u)
    outnum[u] += 1
    outnum[v] += 1
que = deque()
for i in range(N):
    if outnum[i]==1:
        que.append(i)
while que:
    now = que.popleft()
    nxt = G[now][0]
    outnum[now] -= 1
    outnum[nxt] -= 1
    G[nxt].remove(now)
    if outnum[nxt]==1:
        que.append(nxt)

heiro = set()
for i in range(N):
    if outnum[i]!=0:
        heiro.add(i)
Q = INT()
for _ in range(Q):
    a,b = MAP()
    a,b = a-1,b-1
    if a in heiro and b in heiro:
        print(2)
    else:
        print(1)


        

