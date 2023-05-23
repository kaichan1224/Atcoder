from cmath import inf
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
_INPUT = """\
9999 10
540 7550
691 9680
700 9790
510 7150
415 5818
551 7712
587 8227
619 8671
588 8228
176 2461
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
貪欲法で行けそう→成約的にDPです
効率がよい方法:魔力あたりの攻撃力が大きいものから順番に使えば良い
→超えたらOK
→ギリギリ満たさないラインで次に少ない魔力量で条件を満たすものを探す
O(N^2*log(N))でも間に合いそう?
→色々考えたけどめんどくさそうだからO(N^2)で回るしDPじゃね→正解

普通のDPかも？
→個数制限なしナップサック問題!!!! minでそれぞれ更新しよう

一次元dpで考えたほうが楽な問題もあるよ
"""
######################################################
H,N = MAP()
AB = [LIST() for _ in range(N)]
#個数制限なしナップサック
#DP配列を２次元、1次元の両方で考えることができるがわかりやすい１次元で解く
#dp[damage]:=damageを与えるために必要なコスト
dp = [inf]*(H+1)
dp[0] = 0
#与えるのに必要なダメージを少ない順番から
for h in range(H):
    #全ての攻撃に対して一つずつ見ていく
    for damage,cost in AB:
        #この処理も重要！！！
        next_index = min(h+damage,H) #範囲を超えたとき用の処理
        #最小
        dp[next_index] = min(dp[next_index],dp[h]+cost)
print(dp[-1])











