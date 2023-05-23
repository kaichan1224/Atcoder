import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
3
500000000 600000000
600000000 700000000
700000000 800000000





"""
sys.stdin = io.StringIO(_INPUT)
N = INT()
AB = []
d = []
for _ in range(N):
    a,b = MAP()
    a,b = a-1,b-1
    AB.append((a,b))
    d.append(a)
    d.append(b)
dsort = sorted(set(d))
D = { v: i for i, v in enumerate(dsort)}
D2 = { i: v for i, v in enumerate(dsort) }
G = [[] for _ in range(len(D))]
for a,b in AB:
    a2 = D[a]
    b2 = D[b]
    G[a2].append(b2)
    G[b2].append(a2)
if 0 not in D:
    print("1")
    exit()
dist = [False]*(len(D))
dist[0] = True
que = deque([0])
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]==False:
            que.append(nxt)
            dist[nxt] = True
imax = -1
for i,k in enumerate(dist):
    if k==True:
        imax = i
print(D2[imax]+1)









