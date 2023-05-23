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
山登り法は貪欲法などで作った初期解を洗練していく手法
焼きなまし法は山登り法の発展で、山登り法よりも局所解に落ちにくい
遺伝的アルゴリズムは解の多様性を使ってたくさんの解を同時にそれなりに良いものにするアルゴリズム

<ポイント>
・焼きなまし:点数が低くなってもある確率で受け入れる

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

#温度関数
def temperature(time,limit):
    start_temp = 30
    end_temp = 2
    x = time/limit
    return pow(start_temp,1-x)*pow(end_temp,x)

def temperature2(time,limit):
    start_temp = 30
    end_temp = 2
    x = time/limit
    return start_temp + (end_temp - start_temp)*x

def prob(score,new_score,time,limit):
    #スコアは今回は小さい方が望ましい
    d = score - new_score 
    if d>=0:
        return 1
    return math.exp(d/temperature2(time,limit))

Currentscore = score()
epoch = 200000
now_epoch = 0
while now_epoch < epoch:
    #ランダムに反転させる区間を選ぶ
    l = random.randint(1,N-1)
    r = random.randint(1,N-1)
    if l>r:
        l,r = r,l
    P[l:r+1] = reversed(P[l:r+1])
    Newscore = score()
    probability = prob(Currentscore,Newscore,now_epoch,epoch)
    if probability > random.random():
        Currentscore = Newscore
    else:
        P[l:r+1] = reversed(P[l:r+1])
    now_epoch += 1
for p in P:
    print(p+1)


        
        
