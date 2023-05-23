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
3
1 2
2 3

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・頂点の色ではなく、辺の色であることに注意する
・隣ある色が異なる色になるように辺の色を塗る
・多分bfsで解けるけど、情報の保ち方を工夫しないといけないタイプの問題
→ACシマシタ

<キーワード>
・軽めの構築問題、bfs

<ポイント>
・木を扱うときに定番となる考え方として、根を一つ適当に決めるというものがある
"""
#--------------------------------------------------------------
N = INT()
G = [[] for _ in range(N)]
for i in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append((b,i))#繋がっている頂点、辺番号
    G[b].append((a,i))
mlist = [0]*(N-1)
dist = [False]*N
dist[0] = True
que = deque()#(始点、直前に通った辺の色)
que.append([0,-1])
while que:
    now,precolor = que.popleft()
    cnt = 1
    for nxt,vidx in G[now]:
        if dist[nxt]==False:
            dist[nxt] = True
            if cnt==precolor:
                cnt +=1
                mlist[vidx] = cnt
                que.append([nxt,cnt])
            else:
                mlist[vidx] = cnt
                que.append([nxt,cnt])
            cnt += 1
print(max(mlist))
for a in mlist:
    print(a)
        

