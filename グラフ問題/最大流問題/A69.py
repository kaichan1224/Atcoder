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
5
#....
#.#..
....#
....#
..###

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
最大流の計算量はO(N*M^2)
頂点の数N+2じゃないですよ(あほ?)
N*2+視点,終点で2*N+2

<キーワード>
・二部マッチング

<ポイント>
・二部マッチングについて
・計算量はO(N^3)
・条件を満たす辺について全て辺の長さ1で張って、最終的に始点から終点までの最大流量がそのまま答えになる
"""
#--------------------------------------------------------------
class Dinic:
    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None
    #辺の作成
    def add_link(self, _from, to, cap):
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])

    def bfs(self, s):
        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        self.depth = depth

    def dfs(self, v, t, flow):
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0
    
    #最大流を求める
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, float('inf'))
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, float('inf'))
    
N = INT()
C = [list(input()) for _ in range(N)]
#0~N-1が人,N~2N-1が席,2Nが始点,2N+1が終点
dinic = Dinic(2*N+2)
for i in range(N):
    dinic.add_link(2*N,i,1)
    dinic.add_link(i+N,2*N+1,1)
for i in range(N):
    for j in range(N):
        if C[i][j]=="#":
            dinic.add_link(i,N+j,1)
ans = dinic.max_flow(2*N,2*N+1)
print(ans)
            
        
