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
8 1000000000 1000000000
bcdfcgaa




"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------------------------
N,A,B = MAP()
S = input()
INF = float("inf")
if N%2==1:
    #真ん中固定
    center = N//2
    finish = INF
    finish2 = 0
    for i in range(N):
        left = i
        right = i
        cnt = 0
        ans = 0
        if i<center:
            ans = (i + N - center)*A
        else:
            ans = (i - center)*A
        for _ in range(N//2):
            left = (left - 1)%N
            right = (right + 1)%N
            if S[left] != S[right]:
                cnt += 1
        ans += cnt * B
        finish = min(finish,ans)
    left = center
    right = center
    for _ in range(N//2):
        left -= 1
        right += 1
        if S[left]!=S[right]:
            finish2 += B
    print(min(finish2,finish))

else:
    finish = INF
    LEFT = N//2-1
    RIGHT = LEFT+1
    for i in range(N):
        left = i
        right = (i+1)%N
        cnt = 0
        if left<LEFT:
            ans = (left + N - LEFT)*A
        else:
            ans = (left - LEFT)*A
        if S[left]!=S[right]:
            cnt += 1
        for _ in range(N//2):
            left = (left - 1)%N
            right = (right + 1)%N
            if S[left] != S[right]:
                cnt += 1
        ans += cnt * B
        finish = min(finish,ans)
    finish2 = 0
    left = LEFT
    right = RIGHT
    if S[left]!=S[right]:
        finish2 += B
    for _ in range(N//2-1):
        left -= 1
        right += 1
        if S[left]!=S[right]:
            finish2 += B
    print(min(finish2,finish))










