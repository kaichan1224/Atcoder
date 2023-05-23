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
3 14


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
a1+a2+...+an = Mとなる数列aについて,a1,a2,..,anの最大公約数の最大値は?
<考察>
・N進数の和で表せるかを見る?
・素因数分解?

<ポイント>
・答えの候補はMの約数
・すべての要素の公約数としてgがある場合を考える
→すべての要素がgの倍数であればよい
→まず満たすべき条件としてMがgで割り切れる必要がある
→M/g個の要素を各aに分配する必要があるが、最低1つ以上は割り当てる必要がある
→N<=M/g

・分配の仕方は考える必要がない!!!
・すべての要素が１つ以上満たしていれば良い
"""
#--------------------------------------------------------------
def calc_divisors(N):
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
    res.sort(reverse=True)
    return res

def judge(g):
    return N<=M//g #１つ以上分配することができるなら
N,M = MAP()
kouho = calc_divisors(M)
for g in kouho:#候補を大きい順に見て、条件を満たしたらbreak
    if judge(g):
        print(g)
        break
    








