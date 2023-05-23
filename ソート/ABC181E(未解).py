import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
import bisect
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
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・差の合計の最小化
求めるのはi番目のペア((N+1)//2)ペアできる)の身長を（xi,yi）とした時のsum(abs(xi-yi))

・やること
先生の変身形態を選ぶ、最小のペアの組合せを選ぶの二つを考える必要がある。

<キーワード>
・ソート
・貪欲
・にぶたん(ソート済みの適切な部分に値を入れる)

<知識>
・insert(i番目、値x) O(N)
・pop(i番目)：削除 O(N)

<ポイント>
○問題をより簡単な問題に解釈しなおす
・数直線上にN点が存在し、M回のクエリが与えられ各クエリで数直線上の点が一点与えられる
・その点を加えたN+1点を対象にして、二つずつペアを作った時のペアの数値の差の和を最小にしたい
→答えとしては、ソートして貪欲に小さい順からペアを取っていったもの。
→数直線上をイメージしてみると、小さい順からペアを作っていった時に、重複ができないため結果として
差の総和が最小になるのでは?

<ポイント2>
・全ての変身形態wについて、Hの適切な位置にwを挿入して身長の差の合計を求めることで、
安直にやると、O(NM+NlogN)で解ける



"""
#--------------------------------------------------------------
N,M = MAP()
H = LIST()#N(奇数)人の児童の身長
W = LIST()#M個の先生の身長の選択肢
H.sort()

#TLE解
"""
ans = INF
for w in W:
    x = bisect.bisect(H,w)
    #Hをinsertなしで解けるようにしたい(O(N)→O(1)へ)
    H.insert(x,w)
    cost = 0
    #累積和を使ってうまく書き換えたい
    for i in range(0,N,2):
        cost += H[i+1] - H[i]
    ans = min(ans,cost)
    #Hをpopなしで解けるようにしたい(O(N)→O(1)へ)
    H.pop(x)
"""
        


