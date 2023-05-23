import io
import sys
import copy
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
2 3 2
..#
###
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
成約をよく見る→bit全探索
多次元リストの値渡し(深いコピー)はdeepcopyで
"""
######################################################
H,W,K = MAP()
grid = [list(input()) for _ in range(H)]
cnt = 0
for h in product([0,1],repeat=H):
    for w in product([0,1],repeat=W):
        tmp = copy.deepcopy(grid)
        for y in range(len(h)):
            if h[y]==1:
                for x in range(W):
                    tmp[y][x] = 'r'
        for x in range(len(w)):
            if w[x]==1:
                for y in range(H):
                    tmp[y][x] = 'r'
        c = 0
        for y in range(H):
            for x in range(W):
                if tmp[y][x]=='#':
                    c += 1
        if c==K:
            cnt += 1
print(cnt)






