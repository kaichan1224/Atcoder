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
4 1
abac


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
先頭の文字を削除し末尾に追加の任意回数行うことでできる種類数の最小値
<考察>
・なるべく周期を作りたい
<ポイント>
・Aを何回かサイクルしてAと一致
→その列Aはある列Bの何回か繰り返した列
→AはBの倍数
→一致するまでの個数つまり周期数が種類の数(答え)

・文字の長さNについて,Nの約数が変換後の文字列の周期となりうる
→周期が各約数の場合に対して最小操作回数を求める
→K以下であれば答えの候補、Kより大きければ達成できないのでスルー
候補のうち最小値を求める

・Nの約数かつ1<=i<=Mに対して、Si=Si+M=...=Sn-m+iが成り立つ最小のMを
考える時、f(S)=Mとなる
"""
#--------------------------------------------------------------
N,K = MAP()
S = input()
#答えの候補を小さい順番から列挙する
for i in range(1,N+1):#答えの候補となるのは長さの約数となる場合
    if N%i!=0:
        continue
    cnt = 0
    #周期iになるようにするための操作回数を求める
    for j in range(i):#各周期の0番目,1番目,...,i-1番目をi飛ばしで考える
        d = defaultdict(int)
        for p in range(j,N,i):#周期iごとにNまで文字をみる
            d[S[p]] += 1
        #各塊ごとに異なる要素数がどれだけあるかを見る
        cnt += N//i-max(d.values())#(各塊の要素数)-(被っている数(同じ個数))
    if cnt<=K:#周期iにするための操作回数がK以下ならそのとき条件を満たすで答えとなる
        print(i)
        exit()


        










