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


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<山登り法>
・貪欲法などで作った初期解を洗練していく手法
・ある初期解を少しずつ変化させる
1.初期状態　2.状態遷移 3.スコア計算の関数を3つのパーツが必要

<ポイント>
・近傍のスコア計算は差分とって高速に
new_score = score - 部分スコアの変更した部分 + 新たに計算した変更部分のスコア
・状態遷移を高速に
・時間管理は毎回やらなくても良い
"""
#--------------------------------------------------------------
"""
#山登り法1
def scoring(state):
    score = 0
    return score
state = 初期状態
score = 初期状態のスコアを計算

while now_time < limit_time:
    new_state = 近傍を取る
    new_score = scoring(new_state)
    if new_score>score:
        state = new_state
        score = new_score

#山登り法2
def scoring_part(idx, num):
    部分スコアを計算する
    return 部分スコア

state = [3, 1, 4, 1, 5, ..., 9, 2, 6] # 状態
part_score = [scoring_part(idx, state[idx]) for idx in range(len(state))] # 部分スコアを全部保管した配列
score = sum(part_score) # スコアは部分スコアの和とする

t = 0
while 経過時間 < 制限時間:
    num = randint(0, len(state) - 1) # 変更後の数をランダムに決める
    idx = randint(0, 9) # 変更するインデックスをランダムに決める
    # new_stateを必ずしも作る必要はない
    score_plus = scoring_part(idx, num) # idx番目の部分スコアを計算する。
    new_score = score - part_score[idx] + score_plus # 近傍のスコアを少ない計算量で求める
    
    if new_scoreがscoreよりも良い:
        score = new_score
        state[idx] = num # 状態更新も一箇所の変更のみならこれで良い
        part_score[idx] = score_plus # 部分スコアの更新も忘れずに
    
    t += 1
    if tが一定以上:
        t = 0
        経過時間を計測
        # その他頻繁に行う必要のない処理があれば一緒にやる
"""





