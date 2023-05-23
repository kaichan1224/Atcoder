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
<考察>
迂回する必要はない
1->...->1でT分いないといけない。
1->...->1のルートを求めて、「ans = T-かかった時間 * 通った中でmaxの金」の最大が答えになる
無向グラフじゃないから1->sとs->1を同じものとして見れないので、ダイクストラではうまくできないかも?
ダイクストラを1回でできるようにしたかった...
→グラフを逆向きに貼ったやつでdist[s]を求めれば、ダイクストラ2回で計算することができる
sで待つことを考えているので、a[s]でおけ!
"""
#-------------------------------
N,M,T = MAP()
A = LIST()
G = [[] for _ in range(N)]
G2 = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    G[a].append((b,c))
    G2[b].append((a,c))

def dijkstra(G,start):
    N = len(G)
    #距離の管理
    INF = float('inf')
    dist = [INF]*N #スタート地点以外の値は∞で初期化
    #スタート地点の重み（距離）
    #dist[start] = 0 #スタートは0で初期化
    pq = [(INF,start)] #ヒープには(その頂点へのコスト：頂点)の情報が入っている
    cnt = 0
    while pq:
        #ヒープから取り出し
        cnt += 1
        cost,v = heappop(pq)
        if dist[v] != cost: continue
        #最もコストが小さい頂点を探す
        for u,d in G[v]:#G[u]にはつながっている頂点番号とそこへのコストが入っている
            if cnt==1:
                new_cost = d
            else:
                new_cost = cost + d
            #更新条件
            if dist[u] > new_cost: 
                dist[u] = new_cost
                heappush(pq,(new_cost,u)) #pqに(new_cost,u)
    return dist
dist = dijkstra(G,0)
dist2 = dijkstra(G2,0,)

ans = A[0]*T
for i in range(1,N):#中継点
    tmp = max(0,T-(dist[i]+dist2[i]))
    ans = max(ans,tmp*A[i])
print(ans)






