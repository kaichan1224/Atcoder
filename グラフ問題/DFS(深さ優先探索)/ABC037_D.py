import io
import sys
sys.setrecursionlimit(10**9)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations
from functools import lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
mod = 10**9+7
#mod = 998244353
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
######################################################
_INPUT = """\
2 3
1 4 5
2 4 9
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
移動経路の個数数え上げ
→DPの遷移 or dfsメモ化再帰 を最初に思いつく必要がある

メモ化再帰のpypyとpythonの判断
→数値演算の多い(大きい)DP(メモ化)だとTLE
→再帰呼び出しが多すぎるとpypyでTLE

#メモ化再帰のポイント
1.予めmemo配列を準備しておく
2.メモの中身がない(未使用)ときは新たに再帰関数を組み合わせて計算し、
　計算結果をメモしてreturn
　また、初期値をdfs内で設定することもあり。
3.メモが使用済みの場合は、そのままメモをreturnする
4.dfs(x,y)のメモ化再帰でreturn するのはmemo[y][x]である
(returm memo[ny][nx]はイミフ)
5.帰りがけ、行きがけのタイミングに注意
6.再帰だけどpypyで提出しよう(メモ化の場合は呼び出し回数が少ない)
"""
######################################################
H,W = MAP()
grid = [LIST() for _ in range(H)]

memo = [[0]*W for _ in range(H)] 
#dfs(x,y):=(x,y)における移動経路
def dfs(x,y):
    if memo[y][x]!=0:
        return memo[y][x]
    #ここを通過するときはmemoがまだ未使用のときなので
    memo[y][x] = 1    
    for dx,dy in dirc:
        nx,ny = x+dx,y+dy
        if not (0<=nx<W and 0<=ny<H):
            continue
        if grid[y][x]<grid[ny][nx]:
            memo[y][x] += dfs(nx,ny)
    memo[y][x]%=mod
    return memo[y][x]
    

for y in range(H):
    for x in range(W):
        dfs(x,y)
ans = 0        
for y in range(H):
    for x in range(W):
        ans += memo[y][x]
        ans %= mod
print(ans)



