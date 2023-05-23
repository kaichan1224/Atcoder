import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
4
1 1048577
1 1
2 2097153
2 3


"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<ポイント>
・経路圧縮
ある頂点の根を知りたい時に、初めは愚直に親をたどり、
帰りがけに各頂点の辺を直接繋ぎ直すことで高速化

<問題のポイント>
・A[h mod N]!=-1の間,h++
→愚直にやると時間がかかりそう
h++の部分を


"""
#-------------------------------
N = 2**20
Q = INT()
A = [-1]*N
#自分に近い書き換えられていない番号を見つけるための補助配列
P = [0]+list(range(N))
for _ in range(Q):
    t,x = MAP()
    if t==1:
        h = x%N
        pos = h
        visited = [pos]
        while A[pos]!=-1:
            pos = P[pos]
            visited.append(pos)
        A[pos] = x
        newp = P[(pos+1)%N]
        for u in visited:
            P[u] = newp
    else:
        print(A[x%N])




