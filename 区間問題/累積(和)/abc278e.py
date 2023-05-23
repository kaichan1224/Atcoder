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
3 4 5 2 2
2 2 1 1
3 2 5 3
3 4 4 3
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
・フィルタ以外の部分の数字の種類の個数
・愚直にやるとどうなるか
k,l全探索するのにO(hw)=10**5程度,つぶした範囲の色の個数でh,wかけると間に合わない
→累積和的に求めたい。
・種類ごとに累積和を取るアイデアがあるか

・複雑な問題ほど、最大どのくらいの計算量いけるのか、制約をきちんと見る!!!!!

・Aijの種類は高々、N=300なのでO(HWN)

・問題文の読み違い!!!!

・A[i][j][k]とA[i][j][k+1]はアクセスが近いがA[i][j][k]とA[i+1][j][k]はアクセスが遠いので
for i in range(I):
    for j in range(J):
        for k in range(K):
            A[i][j][k]
のようにアクセスしないと普通にTLEする!!!!!!!!!!ので多次元配列では要注意!
"""
#-------------------------------
H,W,N,h_,w_ = MAP()

A = [LIST() for _ in range(H)]
count = [[[0 for _ in range(N+1)] for _ in range(W+2)] for _ in range(H+2)]

for h in range(H):
    for w in range(W):
        for n in range(1,N+1):
            if A[h][w]==n:
                count[h+1][w+1][n] = 1

#まずは横方向
for h in range(1,H+1):
    for w in range(2,W+1):
        for n in range(1,N+1):
            count[h][w][n] += count[h][w-1][n]

#次に横方向
for w in range(1,W+1):
    for h in range(2,H+1):
        for n in range(1,N+1):
            count[h][w][n] += count[h-1][w][n]

B = [[0]*(W-w_+1) for _ in range(H-h_+1)]

for k in range(1,H-h_+2):
    for l in range(1,W-w_+2):
        ans = 0
        for n in range(1,N+1):
            cnt = count[H][W][n]-(count[k+h_-1][l+w_-1][n]-count[k+h_-1][l-1][n]-count[k-1][l+w_-1][n]+count[k-1][l-1][n])
            if cnt>0:
                ans += 1
        B[k-1][l-1] = ans

for h in range(H-h_+1):
    for w in range(W-w_+1):
        print(B[h][w],end=" ")
    print()