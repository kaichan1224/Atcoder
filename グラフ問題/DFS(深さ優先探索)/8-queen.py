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


"""
#--------------------------------------------------------------
N = int(input())
ans = 0
board = [[0]*N for i in range(N)]
def check(y,x):
    flag = False
    for dy in range(-1,2):
        for dx in range(-1,2):
            for k in range(1,N+1):
                ny = y+k*dy
                nx = x+k*dx
                if not (0<=ny<N and 0<=nx<N):
                    break
                if board[ny][nx]==1:
                    flag = True
    if flag:
        return True
    else:
        return False
def display():
    for y in range(N):
        for x in range(N):
            print(board[y][x],end=' ')
        print()
    print()

def dfs(x):
    global ans
    if x==N:
        ans += 1
    else:
        cnt = 0
        for y in range(N):
            if check(y,x)==False:
                board[y][x] = 1
                dfs(x+1)
                board[y][x] = 0
            else:
                cnt += 1
dfs(0)
print(ans)








