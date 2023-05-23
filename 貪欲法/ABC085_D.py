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
4 1000000000
1 1
1 10000000
1 30000000
1 99999999
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
考察
*メモ化再起orDPor貪欲
*Aの中でもっとも大きいものを使い続けたときの回数よりは小さい

貪欲で解ける
maxより大きい方なはなるべく投げ、余ったら残りは一番強い刀を使う
"""
######################################################

N,H = MAP()
AB = [LIST() for _ in range(N)]
ma = max([x[0] for x in AB])
AB.sort(reverse=True,key=lambda x:x[1])
i = 0
cnt = 0
while(H>0):
    if i==N or AB[i][1]<ma:
        break
    H -= AB[i][1]
    cnt += 1
    i += 1
if H>0:
    cnt += (H-1)//ma+1#切り上げの処理注意
print(cnt)







