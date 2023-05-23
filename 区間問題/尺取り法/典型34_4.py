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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
10 2
1 2 3 4 4 3 2 1 2 3

"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
尺取り法(deque)
要素の個数の数え上げは辞書(defaultdict)で行う
d[i]+=1

注意
要素の取り除くときd[i]-=1を行えば良いが、要素の種類数を取得したいときに
d[i]=0のときもカウントされてしまうため、d[i]=1のときは
d.pop(指定キー)とすることで、そのキーごと削除することが可能。
"""
######################################################
N,K = MAP()
A = LIST()
q = deque()
cnt = 0
d = defaultdict(int)
ans = 0
for c in A:
    q.append(c)
    d[c] +=1
    while not(len(d)<=K) and len(q)>0:
        rm = q.popleft()
        if d[rm]>1:
            d[rm] -= 1
        else:
            d.pop(rm)
    ans = max(ans,len(q))
print(ans)




