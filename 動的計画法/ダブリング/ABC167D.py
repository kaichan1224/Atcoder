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
_INPUT = """\
4 5
3 2 4 1




"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<ポイント>
・ダブリングについて
全体の要素数がN個あって1回移動したときにどの要素に到達するのか定まっているとき、
K個先の要素を求めるのにO(K)かかるような状況において、
前処理:O(NlogK)
クエリ:O(logK)
で行うことができるようにするアルゴリズム

前処理：
doubling[k][i] : i 番目の要素から 2^k 先の要素は何か」を以下の式を利用して計算
doubling[k+1][i] = doubling[k][doubling[k][i]]

クエリ：前処理した結果を利用して K 個先の要素を求める
現在地を now として、K を2進数として見た時の全ての桁について以下を行う
K の k 桁目 が 1 ならば now = doubling[k][now] とする

<わかりやすく>
・愚直にK回の遷移について,+1,+1,+1とやると当然間に合わない
→ダブリングにより、+1,+2,+4というように遷移を行うことができる

・dp[p][cu]:現在頂点cuにいて、そこから2^p回遷移したときの遷移先
・初期値はdp[0][cu] = A[cu]
・dpの遷移はdp[p][cu] = dp[p-1][dp[p-1][cu]]
dp[p-1][cu]は頂点cuから2^(p-1)回遷移したときの遷移先であり、
dp[p-1][dp[p-1][cu]]とするとそこから更に2^(p-1)回遷移したときの遷移先と成る。

2^(p-1)+2^(p-1)=2*(2^(p-1))=2^pなので2^p回遷移した先を代入することができる

・求める値(K回の移動先)Kを2進数で考えたときの各桁についてループを回し、
bitが立っているとき遷移するとよい
"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
doubling = [[0]*N for _ in range(100)]
for i in range(N):
    doubling[0][i] = A[i]-1 #0-index
#2^k回遷移したときの遷移先 10**18 = 2 ** 100なのでk=100ぐらいまで考えれば良い
for k in range(1,100):
    for i in range(N):
        doubling[k][i] = doubling[k-1][doubling[k-1][i]]

p = 0
for i in range(100):
    if (K>>i) & 1 == 1:#ここミスらせてた
        p = doubling[i][p] #現在頂点pにいて2^i回遷移したときの遷移先をpでどんどん更新していく
print(p+1) #i-indexに戻す





