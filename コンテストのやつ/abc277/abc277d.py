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
3 10
10 10 10
"""
#連続領域の長さとして最大の部分を求めたい(長さがN超えたら終わり!!!!)
sys.stdin = io.StringIO(_INPUT)
N,M = MAP()
A = LIST()
sumA = sum(A)
A.sort()
B =A + A
allr = []
flag = False
ans = sum(A)
print(ans)
if N==1:
    print(0)
    exit()
for idx,b in enumerate(B):
    if flag==False:
        r = []
        r.append(b)
        now = b
        flag = True
        print(idx,1)
    else:
        #print(f"r:{r},b:{b},now:{now}")
        if (b==now or b==(now+1)%M) and len(r)<N:
            print(idx,2)
            r.append(b)
            now = b
        else:
            print(idx,3)
            #print(sum(r))
            ans = min(ans,sumA-sum(r))
            print(r)
            r = []
            r.append(b)
            now = b
print(ans)







