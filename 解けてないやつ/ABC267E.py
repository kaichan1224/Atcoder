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
7 13
464 661 847 514 74 200 188
5 1
7 1
5 7
4 1
4 5
2 4
5 2
1 3
1 6
3 5
1 2
4 6
2 7


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・最大値の最小化→にぶたん??
・問題の概要を掴むところから始めないと。
・N回の操作全体のコストを一回ごとの操作におけるコストのうちの最大値として定めますの意味がよく分かってなかった
→グラフから頂点を一つづつN個削除するのだが、直接繋がっていてかつまだ削除されていない頂点に書かれている
整数の総和のうち一番大きかった時の値をスコアとして定め、そのスコアの最小値を求める。

<キーワード>
・問題の意味を理解する
・貪欲 or 答えでにぶたん
・heapq

<ポイント>
・「現時点でコストが最も低い頂点に対して操作を行う」貪欲をN回繰り返すのが最適。
・ N =10**5
・多次元配列のヒープの作り方
→最小(最大)を取り出したいのを先頭に持ってきてあとは構成するだけでおけ
"""
#--------------------------------------------------------------
import heapq
class Heapq:
    #最大値を取り出したいときは、desc=Trueにする
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
    #最大or最小を取り出す
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
    #値を追加する
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
    #最大or最小を参照するだけ(なくならない)
    def top(self):
        return self.hq[0] * self.sign
    
N,M = MAP()
A = LIST()
G = [[] for _ in range(N)]
cost = [0]*N
for _ in range(M):
    u,v = MAP()
    u,v = u-1,v-1
    G[u].append(v)
    G[v].append(u)
    cost[u] += A[u]
    cost[v] += A[v]
ver = [[cost,v] for v,cost in enumerate(cost)]
hq = Heapq(ver)
for _ in range(N):
    s,v = hq.pop()
    if cost[v]!=s:
        continue
    ans = max(ans,s)
    for u in G[v]:
        cost[u] -= A[v]
        

    

    

    


        
    
    