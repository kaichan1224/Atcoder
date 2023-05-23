import io
import sys
sys.setrecursionlimit(10**9)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
考察すると、入れ替える部分の除く配列が単調増加であれば良い
→入れ替える回数を減らす＝部分増加列の最も長いものを探す
となりLISで解ける
"""
######################################################
from bisect import bisect_left
def lis(A: list):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            # Lの末尾よりaが大きければ増加部分列を延長できる
            L.append(a)
        else:
            # そうでなければ、「aより小さい最大要素の次」をaにする
            # 該当位置は、二分探索で特定できる
            L[bisect_left(L, a)] = a
    return len(L)

N = INT()
C = [INT() for _ in range(N)]
print(N-lis(C))