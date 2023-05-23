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
<考察>
条件を満たす部分を先頭から順番に考えていく尺取法を考えていた
→前後から尺取するコードで通ったけど多分嘘解法

<ポイント>
・Ai>=0より、累積和は単調増加→二分探索可能!
スタートを固定して、sy-sx=p,sz-sy=q,sw-sz=rである
つまり、sy=sx+pとなるyをにぶたん、sz=sy+qとなるzをにぶたん、sw=sz+rとなるwをにぶたんすればよく

<存在するかの判定>
・単調増加だったらにぶたんが一般的
・setで判定できるものはしたほうがいい(O(1)で可能)

"""
#--------------------------------------------------------------
#setでやる方法
N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

rui = [0]
for i in range(N):
    rui.append(rui[-1] + A[i])

rui_set = set(rui)

for i in range(len(rui_set)):
    Sa = rui[i]
    Sb = P + Sa
    Sc = Sb + Q
    Sw = Sc + R
    #ここの判定を二分探索でやるのももう一つの方法
    if Sb in rui_set and Sc in rui_set and Sw in rui_set:
        print("Yes")
        exit()

print("No")












#これより下嘘解放
"""
q = deque()
tmpsum = 0
ans = [P,Q,R]
idx = 0
flag = False
for c in A:
    q.append(c)
    tmpsum += c
    while not (tmpsum<=ans[idx]) and len(q)>0:
        if idx!=0:
            idx = 0
        rm = q.popleft()
        tmpsum -= rm
    if tmpsum==ans[idx]:
        tmpsum = 0
        idx += 1
    if idx==3:
        flag = True
        break
    
tmpsum = 0
ans = [R,Q,P]
idx = 0
for c in A[::-1]:
    q.append(c)
    tmpsum += c
    while not (tmpsum<=ans[idx]) and len(q)>0:
        if idx!=0:
            idx = 0
        rm = q.popleft()
        tmpsum -= rm
    if tmpsum==ans[idx]:
        tmpsum = 0
        idx += 1
    if idx==3:
        flag = True
        break
if flag:
    print("Yes")
else:
    print("No")
"""

    
