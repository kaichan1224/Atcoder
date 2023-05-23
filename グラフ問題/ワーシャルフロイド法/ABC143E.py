import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float("inf")
#-------------------------------
"""
<考察>
- 全頂点間の最短経路+制限付きでオーダーはO(N^3)でも間に合う。
- s->tで最小化したいのは、補給回数。
- 愚直に実装してみる!
- s->tのL>cなら移動可能、移動後補給することができるのでLnowは固定で問題なし。
- 拡張グラフを考える必要がある?
- 最短距離じゃなくて、最小距離がいい?
- グラフを走りながらDPする系のやつ????
    - そうだったらdp[s][t]で補充回数の最小値を求めたい

<ポイント>
・ギリギリLで行ける部分もコスト1に貼ったグラフを用意し、
これでワーシャルフロイドすれば良い。
・問題が解きやすい形になるように新たにグラフを貼る
"""
#-------------------------------
N,M,L = MAP()
G = [[] for _ in range(N)]
ans:list = [[INF]*N for _ in range(N)]
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    ans[a][b] = c
    ans[b][a] = c

def w(dist):
    for k in range(N):
        for now in range(N):
            for nxt in range(N):
                dist[now][nxt] = min(dist[now][nxt],dist[now][k]+dist[k][nxt])
w(ans)
ans2 = [[INF]*N for _ in range(N)]
for s in range(N):
    for t in range(N):
        if ans[s][t]>L:
            pass
        else:
            #先にワーシャルフロイド法で全頂点間の最短距離を計算しておいたので、それぞれの移動にLがかからない部分をもう一度コスト1と置き直すことができる
            ans2[s][t] = 1
w(ans2)
Q = INT()
for _ in range(Q):
    s,t = MAP()
    s,t = s-1,t-1
    print(ans2[s][t]-1)
