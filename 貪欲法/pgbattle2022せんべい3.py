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
_INPUT = """\
9
4 1 2 1 1 2 3 5 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・1,2,3,...のような数列を消すことができる
・貪欲でやった->WA!

・できるだけ長い部分を消したい
・前から見ていって、順番じゃなくなっても、その間に1,2,..の順番がきちんとできているときは
条件を満たせる?

->右からみるといい?
->後ろからやると上手くいく

<ポイント>
・後ろから貪欲.
・deque使ってうまく管理すると良い。

"""
#--------------------------------------------------------------
N = INT()
A = LIST()
#Bに残っていく
nokori = deque([])
while A:
    print(nokori)
    #右端から見ていく
    a = A.pop()
    if a==1:
        k = 2
        while nokori and nokori[0]==k:
            nokori.popleft()
            k += 1
    else:
        #消せないやつ
        nokori.appendleft(a)
print(sum(nokori))



 



