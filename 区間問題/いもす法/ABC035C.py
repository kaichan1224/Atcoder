import io
import sys
sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
5 4
1 4
2 5
3 3
1 5


"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
・裏表のひっくり返すのは書いた場所だけメモすれば良い。
→いもす、セグメントツリー等で実装できる

・裏表はひっくり返した回数の偶奇で判断することができる
"""
#-------------------------------f
N,Q = MAP()
array = [0]*(N+1)
for _ in range(Q):
    l,r = MAP()
    l,r = l-1,r-1
    array[l] += 1
    array[r+1] -= 1
for i in range(N):
    array[i+1] += array[i] 
ans = ""
for stone in array:
    if stone%2==0:
        ans += "0"
    else:
        ans += "1"
print(ans[:N])






