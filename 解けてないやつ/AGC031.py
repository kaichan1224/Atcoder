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

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
考察
*DPで解けそう?→無理そう
*並び替えることが出来るので注意
*異なる位置からとりだした場合は区別するのに注意
*全ての取り出し方から条件を満たさない場合を引けるか→これっぽいけど考察がまだ
"""
######################################################
N = INT()
S = input()


