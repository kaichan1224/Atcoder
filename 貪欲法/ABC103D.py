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
9 5
1 8
2 7
3 5
4 6
7 9
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・できるだけ重なっているところを切りたい。
-いもす法でやろうとしてけど全然ダメ
→貪欲法の区間スケジューリングっぽい
→だけど実装含めあんまり覚えていないから諦め(FIN)
→勘は合ってたけどACしてないなら意味ない

<キーワード>
・貪欲(スケジューリング問題)
区間の終端でソートして Greedy にとっていけばよい。

・双対性
M 個の区間が与えられ、どの2つの区間も時間帯を共有しないように最大個数の区間を選べ
⇅
まず区間スケジューリング問題の答えが k 個だった場合、その k 個は時間帯を共有しないので、それらを全部刺すには最低でも k 本の串が必要である (弱双対性)
区間スケジューリング問題で選ぶ k 個の区間に対して、その右端から串を刺していけば、ちょうど k 本の串ですべての区間を串刺しにできる (強双対性)

M 個の区間 [ai,bi) が与えられる。
区間を図のようにすべて串刺しにしたい。最小本数の串で区間を串刺しにせよ

<ポイント>
・問題をうまく置き換えることができているか。
・区間スケジューリングの実装方法について。
"""
#--------------------------------------------------------------
N,M = MAP()
imos = [0]*(N+1)
AB = [LIST() for _ in range(M)]
AB.sort(key=lambda x:x[1])
ans = 0
endtime = 0
for i in range(M):
    #予定iの開始時刻が前回終了時刻より遅い場合はそれを採用する
    if AB[i][0]>=endtime:
        endtime = AB[i][1]
        ans += 1
#print(AB)
print(ans)
    

    

    