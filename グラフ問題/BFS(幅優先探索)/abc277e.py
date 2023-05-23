import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
4 4 2
4 3 0
1 2 1
1 2 0
2 1 1
2 4

"""
sys.stdin = io.StringIO(_INPUT)
"""
考察
スイッチを押すor移動のどちらかを行うことができる
移動回数の最小値
->移動するのにコスト1,ボタンを押すのにコスト0と考えることができる(AC)
->どうやって実装するか
->点を拡張しよう!!!!!!
->あとは01BFSで
情報の持ち方は色々あります
https://atcoder.jp/contests/abc277/submissions/36468969

"""
N,M,K = MAP()
G = [[] for _ in range(N*2)]
for _ in range(M):
    v,u,a = MAP()
    v,u = v-1,u-1
    #移動のコストは1!!!!!!
    if a==1:#移動可能なもの同士を繋ぐ
        G[v].append((u,1))
        G[u].append((v,1))
    else:#(一時的な)移動不可能同士を繋ぐ
        G[v+N].append((u+N,1))
        G[u+N].append((v+N,1))
S = LIST()
#スイッチを押す操作のコストは0!!!!!!
for s in S:
    s -= 1
    G[s].append((s+N,0))
    G[s+N].append((s,0))
seen = [False]*(N*2)
seen[0] = True
que = deque()
#現在地点,距離
que.append((0,0))
while que:
    now,dist = que.popleft()
    seen[now] = True
    if now==N-1 or now==N-1+N:
        print(dist)
        exit()
    for nxt,cost in G[now]:
        if seen[nxt]:
            continue
        #コスト0の時は左に追加して~
        if cost==0:
            que.appendleft([nxt,dist])
        #そうでない時は右に追加するだけ~
        else:
            que.append([nxt,dist+1])
print(-1)
        

