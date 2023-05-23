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


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
ハッシュ:文字列などのデータを整数値に対応付ける
・ある状態や数列を一意なハッシュ値に変換することでうまく判定や数え上げ
を行うことができる可能性がある
・Zobrist Hashは状態をハッシュ値にするのが得意(部分集合的な表現が得意)


"""
#--------------------------------------------------------------
#数列をハッシュ値に変換するやつ
def hs():
    L = [0]
    S = set()
    A = [int(a) for a in input().split()]
    s = 0
    for i, a in enumerate(A):
        if a not in S:
            S.add(a)
            s = (s + a * (a + 1346) * (a + 9185)) % P
        L.append(s)
    return L
P = 8128812800000059
N = int(input())
X, Y = hs(), hs()
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print("Yes" if X[x] == Y[y] else "No")




