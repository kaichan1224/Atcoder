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
8 12
0 5
1 3
1 6
2 5
2 7
3 0
3 7
4 1
4 2
4 6
6 7
7 0
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・トポロジカルソートのアルゴリズムについて
・トポロジカルソートは、単純有向グラフについて、有向サイクルを含まないと仮定して、
各頂点を辺の向きに沿うように順序づけて並び替えることである
→有向サイクルがある場合は、成り立たないことを利用してサイクル検出に使うことができる!

<アルゴリズム>
・トポロジカルソート後のものを考えると、一番最後が終点となり、その頂点は出次数が0
であることからグラフの向きとは逆に辿っていくことを考える。
・最終的には前から後ろに同じ方向に辺を張れるように頂点を並び替えるわけだが、
後ろから辿っていって、辿った頂点の出自数を-1し(あらかじめ頂点ごとに出次数をメモしておく)
後ろから辿っていった頂点の出自数が0になったら答えにその頂点を追加していく。
（出次数が0の頂点は今後、順番がおかしくなることはないので、答えに追加することができる）
その後、答えの配列は後ろから辿っていった時に順番がおかしくならない順になっているので、
配列を反転させたものが答えになる。
・オーダーに関しては、頂点番号が小さい順になるようにしたかったらソートする必要があるので、
O(NlogN+M)


"""
#--------------------------------------------------------------
N,M = MAP()
G = [[] for _ in range(N)]
#deg[v]:vを始点とする辺の本数(出次数)
deg = [0]*N
for _ in range(M):
    a,b = MAP()
    G[b].append(a)
    deg[a] += 1

que = deque()
for i in range(N):
    G[i].sort()
    if deg[i]==0:
        que.append(i)
        
order = []
while que:
    now = que.popleft()
    order.append(now)
    for nxt in G[now]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            que.append(nxt)

order.reverse()
print(*order)
    
    