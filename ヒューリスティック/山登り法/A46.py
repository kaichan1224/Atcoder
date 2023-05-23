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
7
1 1
4 1
2 5
3 4
3 2
4 2
5 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>
・山登り法

<ポイント>
・貪欲法などで作った初期解を洗練していく手法
・ある初期解を少しずつ変化させる
1.初期状態　2.状態遷移 3.スコア計算の関数を3つのパーツが必要

"""
#--------------------------------------------------------------
import random
N = INT()
XY = [LIST() for _ in range(N)]    
#初期解
P = []
for i in range(N):
    P.append(i)
P.append(0)
#都市pとqの間の距離を求める関数
def distance(p,q):
    return math.sqrt((XY[p][0]-XY[q][0])**2+(XY[p][1]-XY[q][1])**2)
#得点
def score():
    Scoresum = 0
    for i in range(N):
        Scoresum += distance(P[i],P[i+1])
    return Scoresum

Currentscore = score()
epoch = 20000
for _ in range(epoch):
    #ランダムに反転させる区間を選ぶ
    l = random.randint(1,N-1)
    r = random.randint(1,N-1)
    if l>r:
        l,r = r,l
    P[l:r+1] = reversed(P[l:r+1])
    Newscore = score()
    if Currentscore >= Newscore:
        Currentscore = Newscore
    else:
        P[l:r+1] = reversed(P[l:r+1])
for p in P:
    print(p+1)
print(score())


        
        
