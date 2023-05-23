import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
5
3 1 4 1 5
6
3 2
2 3 4
3 3
1 1
2 3 4
3 3
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
ポイント
→必要な情報だけもつ!!!!
・毎回配列を作ると計算量が大きすぎてだめ
・差分をもつアイデアは普通に良くて、差分が0でない部分だけ情報として持てば良い!!!!!!
・特にdefaultdictはないもないとき0だから尚更都合がよき!!!

例外
・セグツリーで更新すればいけそう
"""
#-------------------------------
N = INT()
A = LIST()
Q = INT()
d = defaultdict(int)
for i,a in enumerate(A):
    d[i] = a
atmp = 0
for _ in range(Q):
    query = LIST()
    if query[0]==1:
        x = query[1]
        d = defaultdict(int) #差分が0でない部分だけ情報として持てば良い
        atmp = x
    elif query[0]==2:
        i,x = query[1],query[2]
        i -= 1
        d[i] += x
    else:
        i = query[1]
        i -= 1
        print(d[i]+atmp)
