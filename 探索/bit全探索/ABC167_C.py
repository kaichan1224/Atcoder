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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3 3 10
60 2 2 4
70 8 7 9
50 2 3 9
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
bit全探索
N=22くらいが限界
"""
######################################################
N,M,X = MAP()
CA = [LIST() for _ in range(N)]
ans = INF
#参考書を使用するかしないかbit全探索
for bits in product([0,1],repeat=N):
    flag = True#条件を満たすかどうか
    u = [0]*M#アルゴリズムの理解度
    money = 0#使用金額
    for i in range(N):#N冊の参考書
        if bits[i]==1:#使用する場合
            money += CA[i][0]
            for j in range(1,M+1):
                u[j-1] +=CA[i][j]
    for v in u:
        if v<X:
            flag = False
    if flag:
        ans = min(ans,money)
if ans==INF:
    print(-1)
else:
    print(ans) 



