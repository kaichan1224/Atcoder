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
import copy
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
3
1 2 3
2 3 4
3 4 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・普通にやると2^100で当然間に合うわけがない

<キーワード>
・ビームサーチ:山登り法や焼きなまし法とは全く違うアルゴリズムで貪欲法に近い
・スコアが良い上位複数個の解を使う
・ビーム幅が大きければ大きいほど良いスコアの解が出力される
・実際には実行制限時間やメモリ制限との兼ね合いがあるため、ビーム幅は無難な値を設定することになる

<ポイント>
・ビームサーチ
・スコア計算は丁寧にやりましょう。
"""
#--------------------------------------------------------------
T = INT()
X = [0]*20
def score(state):
    ans = 0
    for j in state:
        if j==0: ans += 1
    return ans
states = [[score(X),X,""]]
beam = 800
for t in range(T):
    p,q,r = MAP()
    p,q,r = p-1,q-1,r-1
    next_states = []
    #1つ前の状態
    for s,state,koudou in states:
        #とりうる行動
        for i in range(2):
            nextstate = copy.deepcopy(state)
            if i==0:
                nextstate[p],nextstate[q],nextstate[r] = nextstate[p]+1,nextstate[q]+1,nextstate[r]+1
                next_states.append([score(nextstate)+s,nextstate,koudou+"A"])
            else:
                nextstate[p],nextstate[q],nextstate[r] = nextstate[p]-1,nextstate[q]-1,nextstate[r]-1
                next_states.append([score(nextstate)+s,nextstate,koudou+"B"])
    next_states.sort(reverse=True)
    states = []
    for next_state_idx in range(min(beam,len(next_states))):
        scores,next_state,a = next_states[next_state_idx]
        states.append([scores,next_state,a])
for i in states[0][2]:
    print(i)
