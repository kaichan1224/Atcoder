import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
from bisect import bisect_right,bisect_left 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
INF = float('inf')
import math
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
5 5
.....
.###.
.###.
.###.
.....

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・黒に塗られた部分が何角形になるか
・白と接する部分=外側の部分を回って、方向転換した回数が答えになる?
・オーダー的にはdfs?
・確かに問題も分かりにくいところあり


<ポイント>
・角の数え方
## または .. の場合に角になる
#.       .#
→2*2マスの正方形領域(H-1)*(W-1)個を全探索すれば良い。
→あんまり深く考える必要はない。

・オーダーがヒントにならない場合も勿論あるので注意!
→制約ギリギリじゃない時も勿論ある。
"""
#--------------------------------------------------------------
H,W = MAP()
grid = [list(input()) for _ in range(H)]
ans = 0
#方向の注意右と下と右下だけ見れば良い。
dirc = [(0,0),(1,0),(0,1),(1,1)]
for h in range(H-1):
    for w in range(W-1):
        cnt = 0
        for dw,dh in dirc:
            nh = h + dh
            nw = w + dw
            if grid[nh][nw] == "#":
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
            
            


            
        