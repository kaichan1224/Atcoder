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

######################################################
"""
*Ai→Biに辺を貼った有向グラフにおいてトポロジカルソートした結果として、
*辞書順最小のものが答えになる
*トポロジカルソートはグラフに閉路がある時不可能、閉路がなければ可能

<トポロジカルソートのアルゴリズム>
1.それぞれの頂点に対して入ってくる辺の数を数える
2.入ってくる辺の数が0の頂点のうち、一番数字が小さいものを記録する
3.2で記録した頂点とそこから伸びる辺を消す
4.2-3を繰り替えし、入ってくる辺の数が0の頂点がなくなったら終了
"""
######################################################
def topologicalsort(N, G):
    import heapq
    in_number = [0] * N #各頂点の枝の本数をカウントするためのリストを用意する
    for i in G:
        for v in i:
            in_number[v] += 1 #頂点vの入次数をカウントする
    S = [] #手順1:空のリストを用意する。
    queue = [i for i in range(N) if in_number[i] == 0] #入次数が0の頂点を記録するためのリストを用意
    heapq.heapify(queue) # リストを優先度付きキューへ
    while queue:
        u = heapq.heappop(queue) #手順2.1：入次数が0の頂点でかつ最小の頂点uを取り出す
        S.append(u) #手順2.2：手順1で作ったリストSに追加しています。
        for u2 in G[u]:
            in_number[u2] -= 1 #手順2.3：uから出ている辺（枝）を削除
            if in_number[u2] == 0: #uから出ている辺を削除していく作業で頂点u2の入次数が0となった場合
                heapq.heappush(queue, u2) #u2はuの候補となる
    return S
N,M = MAP()
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = MAP()
    G[a-1].append(b-1)
S = topologicalsort(N,G)
if len(S)!=N:
    print(-1)
else:
    for i in range(len(S)):
        print(S[i]+1,end=' ')




