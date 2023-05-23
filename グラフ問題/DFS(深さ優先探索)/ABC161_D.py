import io
import sys
sys.setrecursionlimit(10**7)
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
15

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<K番目に小さい値>
1.全列挙してソートして取り出す→DFS
1.priority_queueを使いながら列挙
3.にぶたん


<dfs全探索>
*今回は数列ではなく、数値の全探索として考える
*一番下の桁をt%10で取り出し、値を追加する操作は×10して,取り出した値を足す
という風にすればよい
*探索する計算量の見積もりは重要！
*この処理の場合は、バックトラックは不要！

"""
#--------------------------------------------------------------
K = INT()
ans = []
def dfs(v):
    ans.append(v)
    if len(str(v))>=11:
        return 
    t = v%10 #一番うしろの数字
    if t+1<=9:
        dfs(v*10+t+1)
    dfs(v*10+t)
    if t-1>=0:
        dfs(v*10+t-1)
#開始地点で分岐がことなるので全ての場合でやる必要がある！
for i in range(1,10):
    dfs(i)
ans.sort()
print(ans[K-1])







