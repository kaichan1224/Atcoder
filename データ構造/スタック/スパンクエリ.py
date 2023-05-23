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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
3
3 1 4
4
1
0 1
0 5
1
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<問題概要>
クエリ問題
・Push(v):後ろから要素追加して、自分よりその値が小さくなるまで、左にindexを進め、
その手前を全てその値(v)で置き換える
・sum():要素の総和を出力

<考察>
・クエリ一つあたりO(logN)が限界

<ポイント>
・差分更新+数列圧縮
・最初の数列は[a,1]でよくて、追加するときに個数を変えればいい
・スタックだけだったら普通のリストでもいい
・一番後ろはA[-1]で参照、A.pop()で取り出す
・スタックとかで要素が空になる系の問題は盤兵(あり得ない答え)を入れておくことで
実装を楽にするというテクニックがある
"""
#--------------------------------------------------------------
N = INT()
A = LIST()
Q = INT()

Arle = []
for a in A:
    Arle.append([a,1])

Asum = sum(A)
for _ in range(Q):
    query = LIST()
    if query[0]==0:
        v = query[1]
        cnt = 1
        while len(Arle)>0 and Arle[-1][0]>v:
            val,num = Arle.pop()
            Asum -= val*num
            cnt += num
        Arle.append([v,cnt])
        Asum += v * cnt
    else:
        print(Asum)
        