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
4
0 1 1 0

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
後ろから見るやつ(定番)：前からやることもできるけど相当難しそう。
反転をフラグ管理も重要!


"""
#--------------------------------------------------------------
N = INT()
A = LIST()
q = deque(A)
flag = False 
while q:
    use = False
    print(q)
    if flag==False:
        while(True):
            if len(q)>0 and q[-1]==0:
                q.pop()
                use = True
            else:
                break
        if len(q)>0 and q[0]==0:
            use = True
            q.popleft()
            flag = True  
    else:
        while(True):
            if  len(q)>0 and q[-1]==1:
                q.pop()
                use = True
            else:
                break
        if len(q)>0 and q[0]==1:
            q.popleft()
            flag = False 
            use = True
    if use==False:
        break
if q:
    print('No')
else:
    print('Yes')










