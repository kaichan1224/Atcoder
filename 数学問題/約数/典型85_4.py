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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
42
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
a*b*c=Kとなる(a,b,c)の組み合わせ
a,b,cは必ずKの約数→約数の個数は少ないことを利用して全探索できる
a,bの値が決まったらcの値は一意に定まる

約数列挙をO(√K)で
デバッグ大事
"""
###################################################
# N の約数をすべて求める関数
def yakusu(N):
    # 答えを表す集合
    res = []
    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break
        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue
        # i は約数である
        res.append(i)
        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            res.append(N // i)
    # 約数を小さい順に並び替えて出力
    res.sort()
    return res
    
K = INT()
Klist = yakusu(K)
print(Klist)
k = len(Klist)
ans = 0
for a in range(k):
    for b in range(a,k):
        if not float.is_integer(K/(Klist[a]*Klist[b])):
            continue
        if Klist[b]<=int(K/(Klist[a]*Klist[b])):
            #print(Klist[a],Klist[b],K/(Klist[a]*Klist[b]))
            ans += 1
print(ans)
