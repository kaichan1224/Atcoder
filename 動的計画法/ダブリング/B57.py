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
100 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・1~Nの全てについて、各位の数字の和の自身から引く操作をK回行った時の値を求める
・シュミレーションすると、法則性が見つかるタイプの問題
・10*Kの値から値が10ごとに+9になる.それまでは0
・81->(90)->99 (189->190)
・180->(189)->198 (299->300)
・261->(270)->279 (389->390)
・279->(288)->297 (399->400)
・360->(369)->378 (499->500)
・(509->510),(589->590),(599->600),(609->610)
・(10->9->10->..)ごとにさらに+9する必要がある?
・法則性があるかもしれないけどよくわからん
・ダブリング使えるかも
・O(1)orO(logN)で求めたい->数学解かダブリングぐらいしか候補がない
<ポイント>
・ダブリングでした
https://github.com/E869120/kyopro-tessoku/blob/main/editorial/chap08/chap08.pdf
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ed

・dp[p][cu]:現在頂点cuにいて、そこから2^p回遷移したときの遷移先
・初期値はdp[0][cu] = A[cu] (1<=cu<=N)
#dpの遷移はテンプレ
for p in range(1,100):#2^k先の遷移
    for i in range(N):
        dp[p][i] = dp[p-1][dp[p-1][i]]
#2^100先まで見ることができるので,y日先をこのようにして求めることができる
for i in range(100):
    if (y>>i) & 1 == 1:
        now = dp[i][now]

・初期値が1番重要!!
一回目の<移動先>を初期値にする
"""
def intketasum(n):
    nlist = list(str(n))
    ketasum = 0
    for n in nlist: ketasum += int(n)
    return ketasum
N,K = MAP()
#dp[p][now]:現在nowにいて、そこからp回遷移した先
dp = [[0]*(N+1) for _ in range(50)]
#整数iから1回操作した後の整数をdp[0][i]
for i in range(1,N+1):
    dp[0][i] = i- (intketasum(i))
for k in range(1,50):
    for now in range(1,N+1):
        dp[k][now] = dp[k-1][dp[k-1][now]]
#1~Nのそれぞれについて、K回丁度操作をした時の値を求める
for n in range(1,N+1):
    now = n
    for i in range(48):
        if (K>>i) & 1 == 1:
            now = dp[i][now]
    print(now)
    
    
            
        
    
    
