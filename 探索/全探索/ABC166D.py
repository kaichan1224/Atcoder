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
33


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・a^5-b^5 = (a-b)(a^4+a^3b+a^2b^2+ab^3+b^4)
・aの方が大きい
・a-b = res
・b = a - res
・aを全列挙すればbも決めやすい
・aは成約的に10^4ぐらいで行けそう
"""
#--------------------------------------------------------------
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
    res.sort(reverse=True)
    return res
X = int(input())
res = calc_divisors(X)
for a in range(0,10**4):
    for r in res:
        b = a - r
        if X == a**5-b**5:
            print(f"{a} {b}")
            exit()




