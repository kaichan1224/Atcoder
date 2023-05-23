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
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・LCA使えばO(NlogN)で行ける?
最大コスト=最小コストだったら一意にパスが定まると言える?
→無理、同じコストの場合もあるじゃん!笑

<ポイント>
・連結で閉路を持たない無向グラフのことを森グラフという
・N頂点N辺の連結無向グラフは、サイクルが一個だけある「なもり」グラフ
・連結：繋がっている、単純：多重辺、ループなし
"""
#--------------------------------------------------------------
N = INT()
UV = [LIST() for _ in range(N)]
Q = INT()
for _ in range(Q):
    x,y = MAP()
