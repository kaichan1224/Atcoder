import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_left,bisect_right
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
8
3 1 4 1 5 9 2 6
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・増えて減る部分の最長の長さ
→最長増加部分列だからDP

<ポイント>
・両端から考える(似たテクニックとして三個のものを扱うときは中央の2番目を考えるがある)
・前からの最長増加列と後ろからの最長増加列を前処理して、
その後Pi+Qi-1が求めたい部分の長さになる

<ミス>
・新たに反転させたリストを用意したい場合は、
    newlist = list(reversed(L))
"""
#--------------------------------------------------------------
def lis(A: list):
    #L:最終的な増加列(条件を満たす部分)
    L = [A[0]]
    #num:配列の各要素のその時点の部分列の最長の長さ
    num = [0]*len(A)
    for i in range(len(A)):
        a = A[i]
        if a > L[-1]:
            # Lの末尾よりaが大きければ増加部分列を延長できる
            L.append(a)
            num[i] = len(L)
        else:
            # そうでなければ、「aより小さい最大要素の次」をaにする
            # 該当位置は、二分探索で特定できる
            pos = bisect_left(L,a)
            L[pos] = a
            num[i] = pos + 1
    #長さを返したい場合はlen(L),最長部分増加列自体を返したい場合はL
    return num
N = INT()
A = LIST()
B = list(reversed(A))
a = lis(A)
b = lis(B)
b.reverse()#リストを反転させて最長部分減少列を求めたので、元に戻す
ans = 0
for i in range(N):
    ans = max(ans,a[i]+b[i]-1)
print(ans)
    






