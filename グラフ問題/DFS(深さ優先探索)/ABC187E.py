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
5
1 2
2 3
2 4
4 5
4
1 1 1
1 4 10
2 1 100
2 2 1000




"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・各頂点に整数が書かれた木について
・頂点aからbを通らずに到達できるようなすべての点の整数をc→c+xに置き換える

<ポイント>
・部分木にすべてxを足すような問題
1.今いる頂点の部分木にすべて足す場合は、今いる頂点に+xして最後にいもすすれば良い
2.今いる頂点の根側の部分木にすべてを足す場合は、全体に+xして、今いる頂点に-xして
いもすすれば1と同じやり方で解ける

<注意>
・どの点からいもすすればいいか注意する
・A,Bは直接つながっている2頂点なのでa,bの距離関係に注意していもすする順番を考える
"""
#--------------------------------------------------------------
N = INT()
G = [[] for i in range(N)]
A = []
B = []
for i in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    A.append(a)
    B.append(b)
    G[a].append(b)
    G[b].append(a)
Q = INT()
C = [0]*N
tmpsum = 0
dist = [-1]*N
dist[0] = 0
que = deque()
que.append(0)
while que:
    now = que.popleft()
    for nxt in G[now]:
        if dist[nxt]==-1:
            dist[nxt] = dist[now] + 1
            que.append(nxt)
print(dist)
for i in range(Q):
    t,e,x = MAP()
    e -= 1
    a,b = A[e],B[e]
    if t==1:#A→B以外
        if dist[b]>=dist[a]:
            C[b] -= x
            tmpsum += x
        else:
            C[a] += x
    else:
        if dist[a]>=dist[b]:
            C[a] -= x
            tmpsum += x
        else:
            C[b] += x

def dfs(v,pre):
    for u in G[v]:
        if u!=pre:
            C[u] += C[v]
            dfs(u,v)
dfs(0,-1)
for i in range(N):
    print(C[i]+tmpsum)







