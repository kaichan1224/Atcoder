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
11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
貪欲法。操作後の最適化問題、やってることはソートして貪欲
もともと小さいやつを書き換えたい、なるべく大きいやつに書き換えたい

Aを小さい順にソート、(C1,,,)..(Cm,,,)を大きい順にソート
各i(0-N-1)に対して、max(A[i],C[i])を合計すればよい
Cの個数がNに満たない場合は、Aの方で補う

B*C=10^14なのでそのまま扱うのはだめ
newc.append((c,b))の形のまま扱う
バグ直しはデバッグを繰り返しておかしいところを探す
"""
#####################################################
N,M = MAP()
A = LIST()
A.sort()
newc = []
cnt_b = 0
for _ in range(M):
    b,c = MAP()
    cnt_b += b
    newc.append([c,b])
newc.sort(reverse=True)
ans = 0
t = 0
flag = False
for i in range(N):
    if i==cnt_b+1:
        flag = True
        tmp = i
        break
    if newc[t][1]!=0:
        flag = False
        if A[i]<newc[t][0]:
            newc[t][1] -= 1
            ans += newc[t][0]
        else:
            ans += A[i]
    else:
        t += 1
        if t==M:
            flag = True
            tmp = i
            break
        flag = False
        if A[i]<newc[t][0]:
            newc[t][1] -= 1
            ans += newc[t][0]
        else:
            ans += A[i]
if flag:    
    for i in range(tmp,N):
        ans += A[i]
print(ans)

