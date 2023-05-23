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
2 0
5 5



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・一つ以上入っている箱の中身を-1する操作を好きなだけできる
・どの隣合う二つの箱の個数の総和がx以下

・貪欲でいけそうに見える?
→なるべく隣あっている部分の箱を減らした方がいい
->i=0,i=N-1の時は内側のものの方がいいし、それ以外はうまく調整すればいける?

・連続した部分列と見ることができるので尺取り法likeな解法でも解ける?

<キーワード>
・貪欲法で問題なし

<ポイント>
ACしました

"""
#--------------------------------------------------------------
import copy
N,x = MAP()
A = LIST()
B = copy.deepcopy(A)
cnt = 0
for i in range(N):
    if A[i]>x:
        A[i] = x
    if i>=1 and A[i]+A[i-1]>x:
        A[i] = x-A[i-1]
ans = 0
for i in range(N):
    ans += B[i]-A[i]
print(ans)
    


