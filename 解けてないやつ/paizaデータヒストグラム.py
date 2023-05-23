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
_INPUT = """\
abcdefg10h12(ij2(3k))l9mnop4(3(2(6(qq)r)s5tu)7v5w)x15(yz)
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""

"""
#--------------------------------------------------------------
def f(x):
    tmp = ""
    for i in x:
        tmp += i
    print(tmp)

from collections import defaultdict,deque
S = input()
new_S = deque()
flag = 0
flag2 = False
prev = deque()
for idx,s in enumerate(S):
    print(f(new_S),s,flag)
    if s=="(" and flag == 0:
        tmp = ""
        while idx>=0:
            idx -= 1
            if S[idx].isdecimal()==False:
                break
            tmp += S[idx]
        tmp = tmp[::-1]
        for i in range(len(tmp)):
            new_S.pop()
        tmp = int(tmp)
        print(tmp)
        flag += 1
    elif s=="(" and flag != 0:
        prev.append(tmp)
        flag += 1
        pre = tmp
        tmp = ""
        while idx>=0:
            idx -= 1
            if S[idx].isdecimal()==False:
                break
            tmp += S[idx]
        tmp = tmp[::-1]
        tmp = int(tmp)
        tmp *= pre
        print(tmp)
    elif s==")":
        if len(prev)!=0:
            tmp = prev.pop()
        else:
            tmp = 1
        flag -= 1
    if s=="(" or s==")":
        continue
    if flag!=0:#(が以前にある状態
        if s.isdecimal()==False and flag2==False:#文字の場合
            new_S.append(str(tmp)+s)
        elif s.isdecimal()==False and flag2:
            pre = tmp
            prev.append(tmp)
            tmp = ""
            while idx>=0:
                idx -= 1
                if S[idx].isdecimal()==False:
                    break
                tmp += S[idx]
            tmp = tmp[::-1]
            tmp = int(tmp)
            tmp *= pre
            new_S.append(str(tmp)+s)
            flag2 = False
        elif s.isdecimal():#数字の場合
            flag2 = True
    else:
        new_S.append(s)
print(new_S)