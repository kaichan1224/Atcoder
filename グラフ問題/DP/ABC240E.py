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
mod = 998244353
#--------------------------------------------------------------
"""
<考察>
・長さK+1,A0 = S,AK = T,頂点AiとAi+1がグラフでつながっている、数列Aの中にXは偶数回
出現する
・通り数を求める問題→制約からもDPっぽい?
-グラフを探索?しながらDPする?
・長さK回ループ
・dp[1~N][偶奇]:値が1~Nで探索回数がKの時の時の答え
・N頂点M辺の単純無向グラフなのでそれぞれの辺の個数は高々O(定数)で大丈夫?
↓
・遷移できたから実行したらえらい大きな値が出てきた
→どこがおかしい:k回目の遷移の値はK+1回目以降に反映されないといけないが、
k回目に既に反映されてしまっている
-値をうまく保たせる必要がある
↓
あれ、全然答え違うじゃん(fin)
→値kを偶数回通った時の答えを出力しているが、その他の値が偶数回である保証が全くない(アホ?)
↓
・どうやって対策しましょ
→詰まったら、もう一度文章を読み直して誤読してないかcheck
・問題分の簡素化してみる
今回の問題は「頂点Sから辺をK回通って頂点Tへ行く方法は何通りか、ただし、Xは偶数回出現する」
・dp[頂点][K回][偶奇判定]
↓
遷移考え直そう!
角頂点を回数ごとにみるのでO(NK),グラフからの遷移は単純無向グラフの高々N頂点なので計算量はほぼ定数
よって間に合う。
↓
答え合わないよ????
↓
問題誤読(全ての頂点が偶数回出現するのではなく、整数Xが偶数回出現する!!!!!)
↓
DP配列の理解し直しが必要!
dp[頂点][K回][頂点Xの偶奇判定]
↓
v == Xかどうかで遷移を場合分けする
(Q.E.D.)

<キーワード>
・単純無向グラフ=木じゃないよ!
ループ,多重辺がない無向グラフのこと
ループ:自分の点から自分の点への辺
多重辺:始点と終点が同じ辺が二つ以上ある時の辺

<ポイント>
・多次元配列の定義の仕方について
dp = [[[0]*2 for _ in range(K+1)] for _ in range(N+1)]
dp[N][K][2],一番端から決まっていく。

・多次元配列の高速化云々の話
最内次元以外の要素数の積と考えても同じです。
つまりA[N][M][L] A[N][M][L]の場合、
NxMxL NxMxLが同じなら一番内側のLが大きいと速く、小さいと遅くなります。
- これで永遠にTLEが取れなかった!!!!!!!!!!!(ガチギレ)
"""
#--------------------------------------------------------------
N,M,K,S,T,X = MAP()
G = [[] for _ in range(N+1)]
edges = []
for _ in range(M):
    u,v = MAP()
    G[u].append(v)
    G[v].append(u)
    edges.append([u,v])
#これはだめ!!!!!!(内側(深い部分)が値が大きい方がいい)
#dp = [[[0]*2 for _ in range(K+1)] for _ in range(N+1)]
dp = [[[0]*(N+1) for _ in range(K+1)] for _ in range(2)]
dp[0][0][S] = 1
for k in range(K):#k回通る
    for now in range(1,N+1):#n頂点目に着目
        for nxt in G[now]:
            if nxt == X:
                dp[1][k+1][nxt] += dp[0][k][now] % mod
                dp[0][k+1][nxt] += dp[1][k][now] % mod
            else:
                dp[1][k+1][nxt] += dp[1][k][now] % mod
                dp[0][k+1][nxt] += dp[0][k][now] % mod
print(dp[0][K][T]%mod)
            
            


