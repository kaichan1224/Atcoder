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
3 3
#..
..#
...

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
1*2のマスでタイルを埋め尽くしたい
→マスを偶奇で黒白で分けて考えるとき、白と黒の組み合わせ数が
最大何ペア作れるかどうかの二部マッチング問題に帰着することが出来る

ペアを復元するときは、それぞれの組み合わせが流れるかどうかを
調べるだけでは意味ない→最適なペアではない可能性がある
↓
辺の情報を元に、平面座標だったら点の情報から復元して答える！
"""
######################################################
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
    #流量を調べる
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
N,M = MAP()
grid = [list(input()) for _ in range(N)]
dinic = Dinic(N*M+2)

#h%2==0 and w%2==0 or h%2==1 and w%2==1 のときのマスが白色
#辺の向きは白→黒
#N*Mが白色とつながる始点、N*M+1が黒色とつながる終点
for h in range(N):
    for w in range(M):
        if grid[h][w]=='.':
            #始点及び終点を結ぶ
            if (h%2==0 and w%2==0) or (h%2==1 and w%2==1):
                dinic.add_link(N*M,w+h*N,1)
            else:
                dinic.add_link(w+h*N,N*M+1,1)
            #上下左右4方向見る
            for dy,dx in dirc:
                nh,nw = h+dy,w+dx
                if not (0<=nh<N and 0<=nw<M):
                    continue
                if grid[nh][nw]=='#':
                    continue
                #マスが白色のとき 向きは
                if (h%2==0 and w%2==0) or (h%2==1 and w%2==1):
                    dinic.add_link(w+h*N,nw+nh*N,1)
                
#最大流
print(dinic.max_flow(N*M,N*M+1))







