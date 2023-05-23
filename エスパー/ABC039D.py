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
dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
#--------------------------------------------------------------
_INPUT = """\
4 4
###.
##.#
..##
..##



"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・ブロックが完全に囲まれたような部分ですべて構成されていたらYes
→どうやって実装するか

・長方形がどのような形でも作れたらOK!
→左回りにDFSできたら良い?
→計算量的に多めに見積もってO(n^4)でn=100なので間に合う?
→サイズが2以上の長方形ができたらいい?
→真ん中はどうする?

・結局最初の方針が良さそう
→角と辺と真ん中で場合分けが必要?

<ポイント>
・逆を考える
・パターンを考える→固定観念だめ!
・周りに一つでも黒い画素があったらその点は黒くする
→逆に収縮後に白いマスがあったら収縮前のその周りは絶対白、それ以外は黒で塗る
・あとは一旦考えられる収縮前を、もっかい収縮して入力と一致すればYes,そうでなければNo
"""
#--------------------------------------------------------------
H,W = MAP()
grid = [list(input()) for _ in range(H)]
dist = [["."]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        noneNum = 0
        if grid[h][w]=='.':
            continue
        for dh,dw in dirc2:
            nh = h + dh
            nw = w + dw
            if not (0<=nh<H and 0<=nw<W):
                continue
            if grid[nh][nw]=='.':
                noneNum += 1
        if noneNum==0:
            dist[h][w] = '#'

for h in range(H):
    for w in range(W):
        print(dist[h][w],end="")
    print()








