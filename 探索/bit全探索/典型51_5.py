import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_left,bisect_right
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
40 20 100
1 3 1 3 4 1 3 5 5 3 3 4 1 5 4 4 3 1 3 4 1 3 2 4 4 1 5 2 5 3 1 3 3 3 5 5 5 2 3 5
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
bit全探索はN=20前後なら間にあるが,N=40の場合は2^40=10^12となり間に合わない
→N-40でも、半分全列挙N=40/2=20なら間に合う

<アルゴリズム>
1,N/2ずつの2グループに分けてそれぞれ全列挙
2,2グループ同士を組み合わせるときに高速化→ニブタン
(Aから選ぶ要素を1つに固定した時、条件に合う要素をBから高速に探す)

<考察>
*ちょうどK個選んで、値段の合計がP円以下
*A1,A2について(選んだ個数、値段の合計)
*選んだ個数ごとにdictを作ればいけそう

<ミス>
配列、辞書の範囲に注意！！
"""
#--------------------------------------------------------------
N,K,P = MAP()
A = LIST()
A1 = []
A2 = []
for i in range(N):
    if i%2==0:
        A1.append(A[i])
    else:
        A2.append(A[i])
da1 = defaultdict(list)
da2 = defaultdict(list)
for bits in product([0,1],repeat=len(A1)):
    num = 0
    a1_sum = 0
    for i in range(len(A1)):
        if bits[i]==1:
            num += 1
            a1_sum += A1[i]
    da1[num].append(a1_sum)

for bits in product([0,1],repeat=len(A2)):
    num = 0
    a2_sum = 0
    for i in range(len(A2)):
        if bits[i]==1:
            num += 1
            a2_sum += A2[i]
    da2[num].append(a2_sum)    

ans = 0
for k,i in da2.items():
    i.sort()
for k,i in da1.items():
    i.sort()    
for i in range(len(da1)):#A1の選び方の個数
    #探したい値はda1[i]+da2[K-i]<=Pとなる個数
    for j in da1[i]:
        a = bisect_right(da2[K-i],P-j)
        ans += a    
print(ans)








