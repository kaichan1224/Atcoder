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
3 4 3
1 3 3 100
1 2 2 10
2 3 2 10
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
*成約が小さいことに着目
*各クエリを10**5で処理しなければならない
*全探索で行ける？
<ポイント>
*考えうる単調広義増加数列を全探索するには...
→普通にやると10^10だが枝刈り全探索でもいける
(単調増加がなかったらO(M^N:10^10)だが、実際は(N+M-1)C(N)の計算量,約O(10^10/10!))
→dfsを使って全探索(n重for文は再帰で書ける!!)
<dfsで全探索について>
*多重for文を解消したい→ある条件を満たす数列を全探索するタイプの問題

"""
#--------------------------------------------------------------
N,M,Q = MAP()
ans = 0
def dfs(A):#再帰を最初に呼び出すときは空の配列を引数に入れる
    global ans
    if len(A)==N: #終端条件 n重ループまで回したら処理して打ち切り
        tmp = 0
        for i in range(Q):
            if A[b[i]]-A[a[i]]==c[i]:
                tmp += d[i]
        ans = max(ans,tmp)
        return
    #生成する数列について、数列を生成する数値の範囲を決める!!!    
    if len(A)>0:
        pre = A[-1]
    else:
        pre = 1
    for v in range(pre,M+1):#数列を一列ずつ生成する
        A.append(v)#一手進む
        dfs(A)#探索
        A.pop()#一手戻る
a = []
b = []
c = []
d = []
for _ in range(Q):
    a1,b1,c1,d1 = MAP()
    a.append(a1-1)
    b.append(b1-1)
    c.append(c1)
    d.append(d1)
dfs([])
print(ans)
    






