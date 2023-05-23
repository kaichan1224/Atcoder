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
反転はフラグで管理。
<注意>
・文字列をqueueで管理する場合、
queue = deque(S) と queue([S]) or queue.append(S)で異なるので注意!
一文字ずつdequeに格納したかったら前者。
これで答えが変わってくることがあるので注意

"""
#--------------------------------------------------------------
S = input()
Q = INT()
queue = deque(S)
flag = False
for _ in range(Q):
    qu = input().split()
    if qu[0]=="1":
        if flag:
            flag = False
        else:
            flag = True
    else:
        f,c = qu[1],qu[2]
        if f=="1":
            if flag:
                queue.append(c)
            else:
                queue.appendleft(c)
        else:
            if flag:
                queue.appendleft(c)
            else:
                queue.append(c)
queue = list(queue)
if flag==False:
    ans = "".join(queue)
else:
    ans = "".join(queue[::-1])
print(ans)

    


    
            
        
        