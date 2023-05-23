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
import math
#dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
10
7 9
8 1
9 6
10 8
8 6
10 3
5 8
4 8
2 5


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・グラフの色の塗り方
・両端が黒はだめ→二部グラフ
・スタートが黒or白の二部グラフを作るが黒の部分は白でも良い

<ポイント>
・(白→黒or白),(黒→白)の遷移はOK→遷移を考えることができるといえば,,,?
→DP!!!!,木の上でDP!
・数え上げこそDP!!

<木DPについて>
・dp[v]:=頂点vを根とする部分木について何かしらの値
・dp[1]を計算する際にdp[2].dp[3]利用している(頂点1が一番上)
・DFSの帰りがけ順で計算するとうまくいく
・木DPの結果は頂点0に帰っていくイメージ
・遷移は,dfsだとdp[now] *= dp[nxt]だが子の情報が根に集約していくイメージ

"""
#--------------------------------------------------------------
N = INT()
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
dp = [[1]*N for i in range(2)]
def dfs(v,pre):
    for nxt in G[v]:
        if nxt!=pre:
            dfs(nxt,v)
            dp[0][v] *= (dp[0][nxt] + dp[1][nxt]) 
            dp[1][v] *= dp[0][nxt]
            dp[0][v] %= mod
            dp[1][v] %= mod
dfs(0,-1)
print((dp[0][0]+dp[1][0])%mod)


