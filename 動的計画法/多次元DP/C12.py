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
4 6 1
1 2
1 3
1 4
2 3
2 4
3 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・制約は小さい
・アルゴリズム的なものは思いつかないのでまずは全探索を考えてみる
→工夫できそうだったらDPで計算量を改善する

・情報として知りたい値はどの区間に繋がりが何個あるか
→言い換えると重なりの問題のようにも感じられるのでいもす的に考えることができるのでは?
・普通に無理です

・３重ループまではできる
・区間について考えるので区間DPですか?

・dp[l][r][K]:区間l,rをK個の小説で分割するときの小説の良さの最大値

--うーんわからんfin

<キーワード>
・動的計画法

<ポイント>
・DP[i][j]:現時点でi章までの割り当てが決まっており、i章の最後のページがjページ目
であることを考える。(この時点での小説の良さの最大値)
・score(l,r):lページ目からrページ目までを同じ章にした時の小説の良さの増分とする
・ページ数N:300,章の数K:10

<できなかった考察>
(・ページの始めではなく、終わりだけを考える
(・k章から順番に考えていく
→DPテーブルの定義
・
"""
#--------------------------------------------------------------
N,M,K = MAP()
G = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = MAP()
    G[a].append(b)
    
#現時点でdp[k][j]:k章までの割り当てが確定していて、K章の最後のページがjページ目であることを考える
dp = [[-INF]*(N+1) for _ in range(K+1)]#dpは1-indexにしましょう
dp[0][0] = 0

#(1<=l,r<=N)
def score(l,r):#l~rまでを同じ章にしたときの小説の良さ
    cnt = 0
    for i in range(l,r+1):
        for v in G[i]:
            if v<=r: cnt += 1
    return cnt

#dp[k][r]:k章の終点がrページの時の良さの最大値
for k in range(1,K+1):#k章目
    for i in range(1,N+1):#K章確定している最後のページ
        for r in range(i):#K-1章の時点で最後のページ
            #貰う遷移
            dp[k][i] = max(dp[k][i],dp[k-1][r]+score(r+1,i))
    
print(dp[-1][-1])
        




    