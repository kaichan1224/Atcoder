import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<ポイント>
- 期待値とは:
    - 一回の試行で得られる平均的な値
    - 例:5が20%,10が80%の時,5*0.2+10*0.8=9

- 期待値の線形性
    → 確率変数X1,X2,,Xnがあったとき、
    (X1の期待値)+,,+(Xnの期待値)=(X1+,,+Xn)の期待値
    - 青のサイコロ、赤のサイコロ、青と赤のサイコロを同時に振る時、E(青と赤)=E(青)+E(赤)

- 有効なものが来るまでにカードを引く期待値は有効なカードを引く確率の逆数
    - もう少しわかりやすく....(これは試行回数の期待値のお話.)
    - 確率pの事象Aについて、事象Aが起きるまでに繰り返すとすると、その回数の期待値は1/p
    - じゃんけんで1回目にグーを出す回数の期待値は3回,これは確率の逆数

<考察>
・試行回数の期待値を求める
最初N頂点がバラバラ
一つ目が繋がれる期待値は1/Nの逆数でN回,二つ目までが繋がれる期待値は2/Nの逆数でN/2回,....
これらの線形和を考えれば、Nつ目までの期待値はN+N/2+N/3+...+N/(N-1)となる?
連結数1->連結数2->連結数3->..->連結数N
"""
#-------------------------------
N = INT()
ans = 0
for i in range(1,N):
    ans += N/i
print(ans)
