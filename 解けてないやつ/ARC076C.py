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
from copy import deepcopy
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
?tc????
coder

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・パターン1
文字列が一致する場所があるとき
・パターン2
?の文字列の長さがTよりも長い時
どちらかを満たす場合は、あとは?→aに置き換えれば良い

<ポイント>
辞書順で最小にするためには、文字列の後ろから調べていけば良い!!!!!!
"""
#--------------------------------------------------------------
S = list(input())
T = list(input())

for i in range(len(S) - len(T), -1, -1):
    for j in range(len(T)):
        if S[i + j] != T[j] and S[i + j] != "?":
            break
    else:
        S[i:i + len(T)] = T
        S2 = "".join(S)
        S2 = S2.replace("?", "a")
        print(S2)
        break
else:
    print("UNRESTORABLE")







