import io
import sys
sys.setrecursionlimit(10**7)
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
1 1
-


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<問題概要>
・+:青マス,-:赤マス
・左上に駒一つ
・高橋くんから始める、右か下に動かせ、赤なら-1点,青なら+1点
・どちらかが操作できなくなった時点でゲーム終了。
・交互にマスを操作する
・お互い最適解になるように行動した時のゲームの結果。

<考察>
・スコアの最適解をDPで求めた後、aokiとtakashiのスコアをdp復元?で求めて、
そのスコアの大小で勝敗判定する?→DPはDPだけどこれは全然最適解じゃない
→最適の行動とは言えないのでだめ
→それぞれの最適解をどのように扱うのかか重要になりそう

・h+wが偶数のところと奇数のところを交互に行き来する

<キーワード>
・ミニマックス法

<ポイント>
・ミニマックス法とは?...の前に、ゲーム木探索について知る必要があるがここでは省略。
・どのような場面で使うべきか
→交互着手二人ゲーム
交互ゲームにおいて、全探索可能、盤面評価可能ならαβ法、そうでない場合はMCTSを使うのが良いらしい。
(https://qiita.com/thun-c/items/058743a25c37c87b8aa4#交互着手二人ゲームのクラス設計)

○さまざまなアルゴリズムについて
・minimax
自分も相手も最善手を打ち続けるという前提のもとにシュミレーションし、現状の最善手を打とうという手法。
評価関数について、一般的には先手が有利なほど大きな値、逆に後手が有利なほど小さな値になるように作るのが一般的。
minimax法では、先手は最も大きな評価値の手を選び、後手は最も小さな評価値の手を選ぶ。
→合法手全てを探索することになるため、探索する深さに応じて指数的に探索時間が伸びてしまうという欠点がある。

・negamax
minimax法と動作は全く同じだが、評価値の符号を反転することで、先手番でも後手番でも評価値が最大となる
指し手を選ぶようにする手法。これにより実装が楽になる。

・αβ
negamax法に対して、絶対に採用されることのない手はそれ以上読まないという芝刈りを取り入れることで、探索を
高速化したもの。

<本問題でのポイント>
・上記知識を踏まえると、高橋君の点数-青木君の点数の符号で勝敗が決まる
・一番右下は最終地点なので点数に影響はない→右下から点数が確定しているマスを広げていけば、
最終的に一番左上の点数を確定させることができる!
・ゲーム木系は再帰で実装することが多い。

<メモ化再帰のポイント(再掲)>
1.予めmemo配列を準備しておく
2.メモの中身がない(未使用)ときは新たに再帰関数を組み合わせて計算し、
　計算結果をメモしてreturn
　また、初期値をdfs内で設定することもあり。
3.メモが使用済みの場合は、そのままメモをreturnする
4.dfs(x,y)のメモ化再帰でreturn するのはmemo[y][x]である
(returm memo[ny][nx]はイミフ)
5.帰りがけ、行きがけのタイミングに注意
6.pythonは基本的に遅い!からforループでかける時はそっちで書いた方がいい(今回の教訓)
"""
#--------------------------------------------------------------
H,W = MAP()
grid = [list(input()) for _ in range(H)]
visit = [[False]*W for _ in range(H)]
memo = [[0]*W for _ in range(H)]

def dp(h,w):
    #メモ済みの値（2回目以降）
    if visit[h][w]:
        return memo[h][w]
    visit[h][w] = True
    turn = (h+w)%2
    
    #初期値
    if h==H-1 and w==W-1:
        memo[h][w] = 0
        return memo[h][w]
    #高橋君
    if turn == 0:
        memo[h][w] = -INF
        if h<H-1:
            if grid[h+1][w]=="+":
                memo[h][w] = max(memo[h][w],dp(h+1,w)+1)
            else:
                memo[h][w] = max(memo[h][w],dp(h+1,w)-1)
        if w<W-1:
            if grid[h][w+1]=="+":
                memo[h][w] = max(memo[h][w],dp(h,w+1)+1)
            else:
                memo[h][w] = max(memo[h][w],dp(h,w+1)-1)
        return memo[h][w]
            
    else:
        memo[h][w] = INF
        if h<H-1:
            if grid[h+1][w]=="+":
                memo[h][w] = min(memo[h][w],dp(h+1,w)-1)
            else:
                memo[h][w] = min(memo[h][w],dp(h+1,w)+1)
        if w<W-1:
            if grid[h][w+1]=="+":
                memo[h][w] = min(memo[h][w],dp(h,w+1)-1)
            else:
                memo[h][w] = min(memo[h][w],dp(h,w+1)+1)
        return memo[h][w]
    
ans = dp(0,0)
if ans > 0:
    print("Takahashi")
elif ans < 0:
    print("Aoki")
else:
    print("Draw")
    
INF = 1 << 60

#TLEしない書き方（基本的に同じ）
H, W = map(int, input().split())
A = [input() for _ in range(H)]
dp = [[0] * W for _ in range(H)]
for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if i == H - 1 and j == W - 1:
            dp[i][j] = 0
        else:
            if (i + 1) % 2 == (j + 1) % 2:
                dp[i][j] = -INF
                if i + 1 < H:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + (1 if A[i + 1][j] == '+' else -1))
                if j + 1 < W:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + (1 if A[i][j + 1] == '+' else -1))
            else:
                dp[i][j] = INF
                if i + 1 < H:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + (-1 if A[i + 1][j] == '+' else 1))
                if j + 1 < W:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + (-1 if A[i][j + 1] == '+' else 1))
if dp[0][0] > 0:
    print('Takahashi')
elif dp[0][0] < 0:
    print('Aoki')
else:
    print('Draw')


    
        
        
