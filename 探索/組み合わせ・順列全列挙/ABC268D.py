import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import combinations_with_replacement, product,combinations,accumulate,permutations
from bisect import bisect_right,bisect_left 
import itertools
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
import random
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
2 2
choku
dai
chokudai
choku_dai
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・N-1ヶ所-を入れる場所がある
最大16個までなので、(16-N)個をN-1ヶ所に割り当てる必要がある
・dfsで構築するタイプかも(手遅れごみ)
・8!=4*10**4
<キーワード>

<ポイント>
・何番目の空白に何個というような考え方ではなく、
・空白を入れることができる個数分の"_"を何番目の空白に割り当てるかをcombinationで求める
という考えのもとコンビネーションを実装することで、やりたかったことができる!!!!

・combinations_with_replacementの使い方について
一つ目の引数がどの範囲の値を重複選択するか-今回は、選択する場所(n-1ヶ所)分範囲が必要
二つ目の引数は何個選択するか-今回は、割り振るアンダーバーの個数

・空白を入れる場所がN-1ヶ所あって、割り振るアンダーバーの個数が二つ目の引数個ある
→割り振るアンダーバーについて、割り振るアンダーバが+0個のパターンも考える必要があるので、
空白を入れる場所についての配列を(N-1)+1(*どこにも割り振らない配列の場所)

・重複組合せの列挙の仕方
"""
#--------------------------------------------------------------
#N:文字列の個数、Mは一致するかどうかの文字列の個数
#Xに条件を満たす文字列を作成する(長さは3<=len(X)<=16であることに注意)
N,M = MAP()
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))
slen = 0
for s in S:
    slen += len(s)

sep = ["_"*i for i in range(17)] #空白を入れる個数の候補
for pat in permutations(S):
    blank = [1]*(N)  #空白を入れる個数(文字の個数-1ヶ所入れる部分がある)
    for under in combinations_with_replacement(range(N),16-slen-(N-1)):
        c = []
        for u in under:
            blank[u] += 1
        for i in range(N):
            c.append(pat[i])
            if i!=N-1:
                c.append(sep[blank[i]])
        c = "".join(c)
        if c not in T and 3<=len(c)<=16:
            print(c)
            exit()
        #毎回配列を生成すると遅くなるから、元に戻す
        for u in under:
            blank[u] -= 1
print(-1)
    
        

        
        
 
    

    