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
0 0 1



"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<操作回数の期待値>
・逆数のやつか期待値DP
・dp[i] =(dp[何か]+(回数))*(確率)+(dp[何か]+(回数))*(確率)+...
・どれか100になったらOK

期待値DPのやつで行ける!!!!
dp(a,b,c) = (dp(a+1,b,c)+1)*()
"""
#-------------------------------
A,B,C = MAP()

memo = [[[-1]*101 for _ in range(101)] for _ in range(101)]

def dp(a,b,c):
    if memo[a][b][c]!=-1:
        return memo[a][b][c]
    if a==100 or b==100 or c==100:
        return 0
    memo[a][b][c]=(dp(a+1,b,c)+1)*(a/(a+b+c))+(dp(a,b+1,c)+1)*(b/(a+b+c))+(dp(a,b,c+1)+1)*(c/(a+b+c))
    return memo[a][b][c]

ans = dp(A,B,C)
print(ans)



    


