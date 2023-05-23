import io
import sys
#sys.setrecursionlimit(10**7)
from copy import deepcopy
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
10 8 1
2 7 1 8 2 8 1 8 2 8
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
*連続部分列なので尺取法で行けそう
<ポイント>
*条件を置き換える
*連続区間の最大と最小が決まっている
→範囲に含まれないものは、条件を満たさない
*かつその要素は最大、最小の値がともに含まれる必要がある
*尺取で左を削るときは、while(True):にして条件を満たさないときbreakすればいい
*尺取(deque)でindexが欲しい場合,別の変数を用意して視点を変えて管理すれば良い
<重要1>
*常に条件を満たす数列を作る(分割する)

<重要2>
*それぞれの連続部分列についてXYがともに含まれる列の個数を求めればよい

<最重要>
*条件を満たす連続部分列の右端以降から配列の終わりまでの長さの分、だけ
*左を削っていって条件を満たす間はans += len(A)-R足すことができる

<別解>
*包含定理

"""
#--------------------------------------------------------------
N,X,Y = MAP()
A = LIST()
#条件を満たす連続部分列に分解する
As = []
tmp = []
for a in A:
    if Y<=a<=X:
        tmp.append(a)
    else:
        if tmp:
            As.append(tmp)
            tmp = []
if tmp:
    As.append(tmp)
ans = 0

for c in As:
    if len(c)==1:
        if c[0]==X and c[0]==Y:
            ans += 1
        continue #長さ1の場合は処理を行う必要はない
    q = deque()
    X_cnt = 0
    Y_cnt = 0
    #尺取法で動かす右端は条件を満たす連続区間の右端
    #条件を満たす区間の右端から配列の端までは全て選択することができる
    #条件を満たしたときのそれ以降の右の部分が選択することができる(L,R)の
    #Rの個数になる
    score = len(c)+1
    #尺取り法部分
    for a in c:
        q.append(a)
        score -= 1
        if a==X:
            X_cnt += 1
        if a==Y:
            Y_cnt += 1
        #条件を満たさなくなるまで左を削る    
        while not (X_cnt<=0 or Y_cnt<=0):
            ans += score
            rm = q.popleft()
            if rm==X:
                X_cnt -= 1
            if rm==Y: 
                Y_cnt -= 1
print(ans)
            
        
        












