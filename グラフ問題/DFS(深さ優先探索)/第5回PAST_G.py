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
import random
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3 3
##.
.##
###
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
dfs全探索のコツ!
バックトラックを忘れないように(一つ前の手を復元する)
具体的には
(次のノードへの遷移)
dfs(再帰呼出し)
(一回元に戻す)←忘れがち

<テンプレ>
def dfs(A):
    # 数列の長さが N に達したら打ち切り
    if len(A) == N:
        # 処理
        return() #exit()
    for v in range(M):
        A.append(v)
        dfs(A)
        A.pop()#重要
dfs([])
"""
######################################################
H,W = MAP()
S = [list(input()) for _ in range(H)]
cnt = 0
for h in range(H):
    for w in range(W):
        if S[h][w]=='#':
            cnt += 1

def dfs(y,x):
    if len(keiro)==cnt:
        print(keiro)
        for k in keiro:
            print(k[1]+1,k[0]+1)#なぜ反転したものが正解となるのか
        exit()
    for dy,dx in dirc:
        ny = y+dy
        nx = x+dx
        if not (0<=ny<H and 0<=nx<W):
            continue
        if S[ny][nx]=='#' and visited[ny][nx]==False:
            visited[ny][nx]=True
            keiro.append((nx,ny))
            dfs(ny,nx)
            #深さ優先探索なので戻ってくるとき(正解ではなかったとき)に復元する必要がある
            keiro.pop()
            visited[ny][nx] = False
print(cnt)
for h in range(H):
    for w in range(W):
        if S[h][w]=='#':
            visited = [[False]*W for _ in range(H)]
            visited[h][w] = True
            keiro = [(w,h)]
            dfs(h,w)



    




