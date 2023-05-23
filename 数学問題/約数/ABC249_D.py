import io
import sys
#sys.setrecursionlimit(10**7)
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
10
1 3 2 4 6 8 2 2 3 7

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""


"""
#--------------------------------------------------------------
# N の約数をすべて求める関数
def calc_divisors(N):
    # 答えを表す集合
    res = []
    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break
        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue
        # i は約数である
        res.append(i)
        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            res.append(N // i)
    # 約数を小さい順に並び替えて出力
    res.sort()
    return res
ans = 0
N = INT()
A = LIST()
a_list = [0]*(max(A)+1)
for a in A:
    a_list[a] += 1
for a in A:
    t = calc_divisors(a)
    for i in range(len(t)):
        ans += a_list[t[i]]*a_list[a//t[i]]
print(ans)








