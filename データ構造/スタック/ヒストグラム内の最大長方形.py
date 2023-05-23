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
6
3 1 4 1 5 9
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・面積が最大のものを考えているため、長方形の高さはA0,A1,...のいずれかに一致すると考えることができる

<ポイント>
・各点に対して、自分より右(左)にあって最初に自分より小さくなるものの位置を求めたい
→普通にやるとO(N^2)になってしまう

"""
#--------------------------------------------------------------
N = int(input())
A = list(map(int, input().split()))

lower_left = [0 for _ in range(N)]  # 左方向に伸ばせる限界の位置
st_left = [] # (A_i, i) をペアで持つスタック
# 番兵の処理
st_left.append([0, -1])
# 各 i について、lower_left[i] を高速に求める
for i in range(0, N):
    # スタックの先頭が A_i 未満になるまで、要素を取り出し続ける
    a = A[i]
    while a <= st_left[-1][0]:
        st_left.pop()

    # lower_left[i] を記録して、(A_i, i) をスタックに入れる
    lower_left[i] = st_left[-1][1]
    st_left.append([a, i])

lower_right = [0 for _ in range(N)] # 右方向に伸ばせる限界の位置
st_right = [] # (A_i, i) をペアで持つスタック
# 番兵の処理
st_right.append([0, N])
# 各 i について、lower_right[i] を高速に求める
for i in range(N-1, -1, -1):
    # スタックの先頭が A_i 未満になるまで、要素を取り出し続ける
    a = A[i]
    while a <= st_right[-1][0]:
        st_right.pop()

    # lower_right[i] を記録して、(A_i, i) をスタックに入れる
    lower_right[i] = st_right[-1][1]
    st_right.append([a, i])

ans = 0 # 答えとなる変数
for i in range(N):
    a = A[i]
    l, r = lower_left[i], lower_right[i]

    # i 番目の長方形を完全に包含する最大の長方形は「幅 a 、高さ r - l - 1」
    # その面積が ans より大きいなら、ans を更新する
    S = a * (r - l - 1)
    if ans < S: ans = S

print(ans)

