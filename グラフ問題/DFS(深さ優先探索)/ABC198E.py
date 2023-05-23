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
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・bfsしながら同じ色の頂点がなければ良い。
→同じ色の頂点があれば探索を打ち切る
・他の頂点に関する処理をうまくことができなかった
↓
部分木を考えることになる(?)のでdfsじゃないとだめ?
↓
なんか違うと思ったら誤読していた。頂点1からのパスで同じ色は一色のみではなく、
移動先のパスと同じ色がなければ良いというものである。
<キーワード>

<ポイント>
・頂点を潜るときにcntの自分の色をインクリメントして、離れるときにデクリメントすることで、この配列に入っている情報を
現在見ている頂点から始点（頂点1）までの情報に限定することができる。
"""
#--------------------------------------------------------------
N = INT()
C = LIST()
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
    
col = defaultdict(int)
ans = []

def dfs(now,pre,color):
    color[C[now]] += 1
    if color[C[now]]<2:
        ans.append(now+1)
    for nxt in G[now]:
        if pre!=nxt:
            dfs(nxt,now,color)
    color[C[now]] -= 1
dfs(0,-1,col)
ans.sort()
for a in ans:
    print(a)
