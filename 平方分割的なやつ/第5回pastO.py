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

"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
愚直に実装すると、だめな場合がある
→隣接する頂点がやたら多い頂点が存在する場合

平方分割的な考えを使う
ユーザの友達が√M人以上と未満の場合で処理を変える

ユーザ数M未満の場合
    そのままでOK
そうでない場合が問題
    step1:隣接する友達に配る回数を記録する
    step2:友達√M人以上の人の隣接リストを予め用意
    step3:その中で通知の個数分プラス
    step4:出力は前回との差分にしておくことで初期化処理不要。
"""
#-------------------------------
N,M = MAP()
G = [[] for _ in range(N)]
higherG = [[] for _ in range(N)]
#普通の友達関係
for _ in range(M):
    a,b = MAP()
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
#√M:友達の数の大きさで処理を場合分け:平方分割
rtM = int(M**0.5)
#友達の数が√M人の場合のグラフ
#ユーザxの友達のうち友達が√M人以上いるユーザ
for i in range(N):#iそれぞれについて
    for x in G[i]:#iの友達x
        if len(G[x])>=rtM:
            higherG[i].append(x)
Q = INT()
mail = defaultdict(int)
highermail = defaultdict(int)
before = [0]*N
for _ in range(Q):
    t,x = MAP()
    x -= 1
    if t==1:
        #友達√M人以下
        if len(G[x]<rtM):
            #直接隣接しているユーザに通知
            for v in G[x]:
                mail[v] += 1
        else:
            highermail[x] += 1
    else:
        #友達√M人以下
        ans = mail[x]
        #√M人以上の場合
        #友達が√M人以上の場合の中に通知を配る人がいたら通知の個数分プラスする
        for a in higherG[x]:
            ans += highermail[a]
        #以前の答えの情報を持っておくと、今回の差分を計算しておけば、リセット処理をする必要はない
        print(ans-before[x])
        before[x] = ans






