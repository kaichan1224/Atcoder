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
2 3
1 2 3
0 1 1

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・偶数枚コインが置かれたマスの数を最大化したい
・3枚以上の奇枚のコインは分配する意味があるかも?
↓
全然わからん(FIN)

<キーワード>
・構築問題

<ポイント>
・点数の低い構築問題は機械的にやれる最適戦略がある場合が多い
・今回の問題は操作回数の最小化が求められてないので、簡単な機械化を目指す

・問題の見落としはだめ!!
-まだ選んだことのないマスのうち 1 枚以上のコインが置かれているマスを...

・奇数が偶数枚の時、奇数同士をペアにして奇数を消滅させられる
・奇数が奇数枚の時、一個を除いて奇数を消滅することができる

"""
#--------------------------------------------------------------
H,W = MAP()
grid = [LIST() for _ in range(H)]

                
