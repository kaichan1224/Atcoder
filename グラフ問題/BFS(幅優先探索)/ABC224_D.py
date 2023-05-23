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
"""
有名な問題(8-puzzle)
頂点9が空いている部分なので順番に入れ替える

<バグらせポイント>
*グラフでつながっている部分は、空きコマとつながっている部分の'位置'である
ことに要注意!!!

*パズルのマス情報を文字列として記憶し、その位置(文字列)になったことが
なかったら移動する(空白のマスに移動すればよい)

*マス自体は配列で管理するが位置として管理する場合は文字列じゃないと辞書に
登録できず、逆にマスを入れ替えるときは
"""
#--------------------------------------------------------------
M = INT()
G = [[] for _ in range(9)]
for _ in range(M):
    u,v = MAP()
    G[u-1].append(v-1)
    G[v-1].append(u-1)
#print(G)
p = LIST()#パズルの順番
u = [8]*(9)#コマの順番
for i in range(8):
    u[p[i]-1] = i
u = ''.join(map(str,u))
g = '012345678'#正解の順番
q = deque()
q.append((u,0))
d = defaultdict(int)
d[u] = 0
while q:
    now,cnt = q.popleft()
    if now==g:
        print(cnt)
        exit()
    loca = now.index(str(8))
    for nxt in G[loca]:
        l = list(now)
        #グラフでつながっているのは位置であってコマ自体の番号ではないところに要注意!
        l[nxt],l[loca] = l[loca],l[nxt]
        tmp = ''.join(l)
        if tmp not in d:
            q.append((tmp,cnt+1))
            d[tmp] = 1
print(-1)