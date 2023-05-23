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
"""
pypyだと通るやつ
bit全探索はN=23がギリギリだということを覚えておこう:(
"""
#--------------------------------------------------------------
H1,W1 = MAP()
A = [LIST() for _ in range(H1)]
H2,W2 = MAP()
B = [LIST() for _ in range(H2)]
flag = False
for h in product([0,1],repeat=H1):
    for w in product([0,1],repeat=W1):
        tmp = []
        for i in range(H1):
            if h[i]==1:
                tmp2 = []
                for j in range(W1):
                    if w[j]==1:
                        tmp2.append(A[i][j])
                if len(tmp2)!=0:
                    tmp.append(tmp2)
        if tmp==B:
            flag = True
if flag:
    print("Yes")
else:
    print("No")
        