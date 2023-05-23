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
3 50
3 9 17 
4 7 9
10 20 30
1 2 3

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・a,bは探索可能
・c+d = K-a-bを満たす時、条件を満たす

<キーワード>
・XがAの中にあるかどうかの判定はsetを使えばO(1)で計算することができる
・半分全列挙

<ポイント>
・四個のグループを二つずつのグループに分けてそれぞれ列挙し、組合せ方を高速に求める
工夫をすることでも解くことができる。組合せを求める際ににぶたんをよく使いそのために
ソートするのを忘れないように。
・今回の計算量はO(N^2*log(N))
(どうでもいいけど、(logN)^2の計算量は2logNなのでO(logN)です)
"""
#--------------------------------------------------------------
N,K = MAP()
A = set(LIST())
B = set(LIST())
C = set(LIST())
D = set(LIST())
E = set()
for c in C:
    for d in D:
        E.add(c+d)
flag = False
for a in A:
    for b in B:
        if K-a-b in E:
            flag = True
if flag:
    print("Yes")
else:
    print("No")
                
            
