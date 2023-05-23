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
5
10101
60 45 30 40 80

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・f(X):X未満なら子供0,以上なら大人1で、N人のうち子どもか大人かを正しく判定できる人数
Xが実数全体を動く時、f(X)の最大値

<ポイント>
・Xを全部試す?→実数?→整数だけでよい→さらに言うと体重と体重の境目だけで良い
→順番に見るならソートする必要がある
→Xの候補を10**5にできた!
→あとはf(X)をO(1)かO(logN)で求めることができれば良い!

<ポイント>
・まずは愚直に計算する方法を考えてから、計算量を工夫する
・差分を計算するのはO(1)でできる→そのためにはソートが必要!
・さらに、Wが同じ値の場合の考察をまだできていないので注意!
→紙に書いて考えると、同じ値の場合は考察できないので、次の物が値が変わるまで、tmpの増減を考える必要がない

・増減部分だけを考え、次と同じだったらcontinueそうでなかったら最大値更新を行えば良い

<キーワード>
・計算量工夫のために、扱うべきデータを考える→ソート
・各f(X)をクエリと考えると、差分を考えるテクニックを使えば良い。

・クエリ問題の方針
1.各クエリについて高速に計算
2.全部前計算
3.差分を計算することで高速に計算　←激重要!!!!!!!!!!!!
"""
#--------------------------------------------------------------
N = INT()
S = input()
W = LIST()
P = []
for i in range(N):#正解のペアごとに格納してソートすれば順番に見れる
    P.append([W[i],S[i]])
P.sort(key=lambda x:x[0])

#Xが一番外の状況からずらしていくイメージ
#f(X)は最初だけO(N)で個別で求めてあとは、ずらしてO(1)で。
ans = 0
for i in range(N):
    if P[i][1]=="1":
        ans += 1
tmp = ans
#増減を考える
cnt = 0
for i in range(N):
    w,s = P[i][0],P[i][1]
    if s=="0":
        cnt += 1
    else:
        cnt -= 1
    if i!=N-1 and w == P[i+1][0]:#前と同じ
        continue
    ans = max(ans,tmp+cnt)
print(ans)
        
        
    
    

