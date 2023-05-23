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
4
ooxo

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
ランレングス圧縮を利用、余事象を考えることで楽に問題を解けるように。
"""
######################################################
def rle_num(s): #ランレングス圧縮したときの数値部分のリストを返す
    n = len(s)
    block = []
    num = 0
    for i in range(n):
        num += 1
        if i < n-1 and s[i] != s[i+1]:
            block.append(num)
            num = 0
    else:
        block.append(num)
    return block

N = INT()
S = input()
q = deque()
cnt = 0
for i in rle_num(S):
    cnt += i*(i-1)//2
print(N*(N-1)//2-cnt)





