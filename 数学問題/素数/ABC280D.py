import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
#-------------------------------
"""


"""
#-------------------------------
_INPUT = """\
1024
"""
#-------------------------------
sys.stdin = io.StringIO(_INPUT)
K = INT()
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def f(k):
    t = factorization(k)
    ans = set()
    for num,x in t:
        x -= 1
        ans.add(num)
        tmp = num
        while x>0:
            tmp += num
            ans.add(tmp)
            y = factorization(tmp)
            if len(y)==1:
                x -= y[0][1]
            else:
                for a,b in y:
                    if a==num:
                        x -= b
                        break
    return max(ans)

print(f(K))



        






