import io
import sys
sys.setrecursionlimit(10**9)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
5 7 5
1 2 6
2 3 4
1 3 3
1 4 1
3 4 6
3 5 5
1 5 9
1 5 4 3 5
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
シュミレーション問題、ヒープ

自分がいる可能性のある頂点と可能性のない頂点を結ぶ辺を管理

その中で、通行時間Xi以下の辺がある限り一つ取り出すa
    aの端点のうちあなたがいる可能性がなかった方をxとする
    xをあなたがいる可能性のある頂点としてマークし、
    隣接する辺をみて必要ならSに新たに追加
"""
######################################################
N,M,Q = MAP()
G = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    G[a].append((c,b))
    G[b].append((c,a))
X = LIST()
visited = set()
visited.add(0)
pq = []
q = deque([0])

for i in range(Q):
    #現在つながっている可能性がある都市と可能性のない頂点を結ぶ辺を管理
    while q:
        v = q.popleft()
        for c,nv in G[v]:
            #(辺の重さ、繋ぐ点)で格納
            heappush(pq,(c,nv))
    
    while pq:
        c,nv = heappop(pq)
        if nv in visited:
            continue
        elif c<=X[i]:
            visited.add(nv)
            q.append(nv)
        else:
            heappush(pq,(c,nv))
            break
print(len(visited))

 








