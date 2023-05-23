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
0 0 0
1 1 1
-1 -1 -1


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・順列全探索で行けそうだけどN=8ぐらいまでじゃないと無理
→半分全列挙すればいける?

<ポイント>
bitDP
・ある条件を満たす順列の数え上げに関して、N!では間に合わないが2^Nなら間に合いそう
というときに使えるテクニック。
・計算量をO(N*N!)→O(N^2*2*N)まで落とすことができ、N=19まではぎりぎり通すことができる
・DP[S]:=部分集合Sに対して|S!|通りの順序の中から最適なものを選んだときの何かしらの値
・DP[S U {v}] = dp[S] + cost(S,v)
・集合をbitで表現する

<具体例>
・巡回セールスマン問題
今まで到達都市の順番が{0,2,3,5}のとき残りは{1,4}で最後に0に返ってくるだけ
このような状況は他にも{0,3,2,5}とかがある
→これは、ここまでに辿ってきた街の集合が同じかつ最後に訪れた街が共通している
最後に訪れた街:ただの街番号として覚えておけば良い
ここまでに辿ってきた街の集合:2進数を使用して整数で保持する

計算量について
最後に訪れた街の種類が最大N通り
街の状態数は2^N通り
各状態に対して最大N通りの次の街の選択肢
→O(2^N*N^2)

実装について
DP[S][i]:=現在地が都市iで、訪問済みの街の集合がSであるときのコストの最小値
配るDP:最後の頂点から、探索してない全頂点に対して配るDPを行う

使うbit演算
・1<<N:2**Nのこと
・n>>k & 1:nのk+1桁目が1かどうか(0-indexedなら右からk番目)
・S&T 集合の積
"""
#--------------------------------------------------------------
N = int(input())
XYZ = [LIST() for _ in range(N)]

def calc(i,j):
    xi,yi,zi = XYZ[i]
    xj,yj,zj = XYZ[j]
    return abs(xi-xj)+abs(yi-yj)+max(0,zi-zj)

#すべての状態にINFを入れておく
#dp[j][i]:訪れた都市の状態iにおいて最終的に都市jにいるときのコスト
dp = [[INF]*(N+1) for _ in range((1<<N)+5)]
#初期状態
dp[0][0] = 0#１つ目の都市を訪れていることを表すと000001(一番左のbitがたった状態)

#DP更新
for s in range(1<<N):#集合を添え字の小さい順に試す
    for u in range(N):
        for v in range(N):
            if(s >> v) & 1 and s != 0:
                continue
            dist = calc(v,u)
            if dp[s][u] + dist < dp[s | (1<<v)][v]:#s|(1<<ｖ)
                dp[s | (1<<v)][v] = dp[s][u] + dist
print(dp[(1<<N)-1][0])



n = int(input())
P = [tuple(map(int, input().split())) for _ in range(n)]
C = [[0] * n for _ in range(n)]
for i in range(n):
    xi, yi, zi = P[i]
    for j in range(n):
        xj, yj, zj = P[j]
        C[i][j] = abs(xi - xj) + abs(yi - yj) + max(0, zj - zi)
DP = [[1 << 30] * n for _ in range(1 << n)]
DP[0][0] = 0
for s in range(1 << n):#
    for i in range(n):
        if (1 << i) & s:
            for j in range(n):
                DP[s][i] = min(DP[s][i], DP[s - (1 << i)][j] + C[j][i])
print(DP[(1 << n) - 1][0])
        








