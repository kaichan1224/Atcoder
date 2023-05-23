import io
import sys
sys.setrecursionlimit(10**7)
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
39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB





"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・O(N^2)まで行ける
→真ん中固定で行ける?
・余事象を使う?
・pypyで実行しないと間に合わない
"""
#--------------------------------------------------------------
N = int(input())
S = list(input())
ans = 0
for j in range(1,N-1):
    j_color = S[j]
    if j_color=='R':
        i_color_G = 0
        i_color_B = 0
        k_color_G = 0
        k_color_B = 0
        for i in range(0,j):
            if S[i]=='G':
                i_color_G += 1
            elif S[i]=='B':
                i_color_B += 1
        
        for k in range(j+1,N):
            if S[k]=='G':
                k_color_G += 1
            elif S[k]=='B':
                k_color_B += 1
        ans += i_color_G * k_color_B + i_color_B * k_color_G
        t = min(j,N-(j+1))
        for m in range(1,t+1):
            i = j-m
            k = j+m
            if S[i]!=S[k]:
                if S[i]=='B' and S[k]=='G':
                    ans -= 1
                elif S[i]=='G' and S[k]=='B':
                    ans -= 1
        
    elif j_color=='G':
        i_color_R = 0
        i_color_B = 0
        k_color_R = 0
        k_color_B = 0
        for i in range(0,j):
            if S[i]=='R':
                i_color_R += 1
            elif S[i]=='B':
                i_color_B += 1
        
        for k in range(j+1,N):
            if S[k]=='R':
                k_color_R += 1
            elif S[k]=='B':
                k_color_B += 1
        ans += i_color_R * k_color_B + i_color_B * k_color_R
        t = min(j,N-(j+1))
        for m in range(1,t+1):
            i = j-m
            k = j+m
            if S[i]!=S[k]:
                if S[i]=='R' and S[k]=='B':
                    ans -= 1
                elif S[i]=='B' and S[k]=='R':
                    ans -= 1
    else:
        i_color_R = 0
        i_color_G = 0
        k_color_R = 0
        k_color_G = 0  
        for i in range(0,j):
            if S[i]=='G':
                i_color_G += 1
            elif S[i]=='R':
                i_color_R += 1
        
        for k in range(j+1,N):
            if S[k]=='G':
                k_color_G += 1
            elif S[k]=='R':
                k_color_R += 1
        ans += i_color_G * k_color_R + i_color_R * k_color_G
        t = min(j,N-(j+1))
        for m in range(1,t+1):
            i = j-m
            k = j+m
            if S[i]!=S[k]:
                if S[i]=='R' and S[k]=='G':
                    ans -= 1
                elif S[i]=='G' and S[k]=='R':
                    ans -= 1     
print(ans)
    




