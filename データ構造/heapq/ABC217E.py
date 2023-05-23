import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
#from heapq import heappush,heappop 
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
8
1 4
1 3
1 2
1 1
3
2
1 0
2
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
<考察>
・毎回ソートすると、制約オーバー
・ソート後の先頭の要素は最小値、ソート時点の配列の大きさの範囲までは昇順であることが保証できる

ソート→先頭出力の場合、最小値を出力すればいい
もう少し正しい事を言うと、一度ソートすれば、その配列から最小値を取り続け
その配列から値がなくなれば、deque()から先頭のデータをとればよい
それ以外のときは先頭を出力

ポイント
*データを２本で管理する
*ヒープの長さについて、長さは持ってるライブラリだとわからない？が
if hq:と書くことで存在するかどうかを処理することが出来る
*償却解析:クエリ全体での計算量を解析すること

(関係ないけど同じファイル内にheapq.pyがあるとimportがうまくいかないので注意)
"""
######################################################
import heapq
class Heapq:
    #最大値を取り出したいときは、desc=Trueにする
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
    #最大or最小を取り出す
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
    #値を追加する
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
    #最大or最小を参照するだけ(なくならない)
    def top(self):
        return self.hq[0] * self.sign

Q = INT()
A1 = deque()
T = []
A2 = Heapq(T)
for _ in range(Q):
    query = LIST()
    if query[0]==1:
        x = query[1]
        A1.append(x)
    elif query[0]==2:
        if A2:#A2が長さ0かどうかはこうやってかく
            print(A2.pop())
        else:
            print(A1.popleft())
    else:
        while A1:
            A2.push(A1.pop())



