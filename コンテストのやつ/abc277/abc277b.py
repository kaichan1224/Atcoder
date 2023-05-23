import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\








"""
sys.stdin = io.StringIO(_INPUT)
N = INT()
flag = True
s = set()
for _ in range(N):
    S = input()
    if S in s:
        flag = False
    else:
        s.add(S)
    if not (S[0]=="H" or S[0]=="D" or S[0]=="C"or S[0]=="S"):
        flag = False
    if not (S[1]=="A" or S[1]=="2" or S[1]=="3" or S[1]=="4" or S[1]=="5" or S[1]=="6" or S[1]=="7" or S[1]=="8" or S[1]=="9" or S[1]=="T" or S[1]=="J" or S[1]=="Q" or S[1]=="K"):
        flag = False
if flag:
    print("Yes")
else:
    print("No")