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
6 7
5 3
1 7 12 19 20 26
4 9 15 23 24 31 33
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
まず貪欲を考え,早い物順に使えるものがあったら使う
時間ベースで考えるとTLE
空港のindexでシュミレーションで解ける(AC)

<解説>
別解：時刻をにぶたんで高速で求める
"""
#--------------------------------------------------------------
N,M = MAP()
X,Y = MAP()
A = LIST()
B = LIST()
useA = [False]*N
useB = [False]*M
tmp = 0
a_index = 0
b_index = 0
ans = 0
while(True):
    #print(tmp)
    if a_index==N:
        break
    if b_index==M:
        break
    if A[a_index]>=tmp:
        tmp = A[a_index]+X
        a_index += 1
        ans += 1
    else:
        a_index += 1
        if a_index==N:
            break
        while(A[a_index]<tmp):
            a_index += 1
            if a_index==N:
                break
        if a_index==N:
            break
        tmp = A[a_index]+X
        ans += 1
    #print(tmp)
    if B[b_index]>=tmp:
        tmp = B[b_index]+Y
        b_index += 1
        ans += 1
    else:
        b_index += 1
        if b_index==M:
            break  
        while(B[b_index]<tmp):
            b_index += 1
            if b_index==M:
                break
        if b_index==M:
            break    
        tmp = B[b_index]+Y
        ans += 1
print(ans//2)

    

    

    
        










