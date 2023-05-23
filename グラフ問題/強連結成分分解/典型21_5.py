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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
100 1
1 2

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
強連結成分分解
有向グラフにおいて、お互いに行き来できる⇔同じグループを満たすように
グループ分けすること
→非DAGをDAGにすることができる

計算量O(N+M)
"""
######################################################
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)#各頂点に対して頂点から進めなくなった順番を格納
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)#行き止まったところまでを一つの連結成分とする   
    for i in range(N):
        if not used[i]:
            dfs(i)#適当な頂点から深さ優先探索を行う
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)#グラフの向きを全て逆にしたものに対して深さ優先探索
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP
N,M = MAP()
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]
for _ in range(M):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    RG[b].append(a)

label,group =scc(N,G,RG)
G0,GP = construct(N,G,label,group)
ans = 0
for p in GP:
    ans += len(p)*(len(p)-1)//2
print(ans)







