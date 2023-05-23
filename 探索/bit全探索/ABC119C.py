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
_INPUT = """\
5 100 90 80
98
40
30
21
80
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・4本以上の場合は3本になるまで接続する
→使わなくてもいい竹もあるのでA,B,C,使わないのbit全探索を考えれば良いO(4^N)

<ポイント>
・+1,-1するのは合体を完全にやりきった後からで良い
・+1するのも-1するのもコストは1なのでかかルコストは絶対値の差をとれば求めることができる
・合体して三本を作り出す方法は,bit全探索もしくは再帰で書くことができる

"""
#--------------------------------------------------------------
N,A,B,C = MAP()
l = [INT() for i in range(N)]
a,b,c = 0,0,0
ans = float('inf')
for bits in product([0,1,2,3],repeat=N):
    a,b,c = 0,0,0
    cnta,cntb,cntc = 0,0,0
    for i,item in enumerate(bits):
        if item==0:#a
            a += l[i]
            cnta += 1
        elif item==1:#b
            b += l[i]
            cntb += 1
        elif item==2:#c
            c += l[i]
            cntc += 1
    if a>0 and b>0 and c>0:
        tmp = float('inf')
        tmp = min(tmp,abs(a-A)+abs(b-B)+abs(c-C))
        tmp = min(tmp,abs(a-A)+abs(b-C)+abs(c-B))
        tmp = min(tmp,abs(a-B)+abs(b-A)+abs(c-C))
        tmp = min(tmp,abs(a-B)+abs(b-C)+abs(c-A))
        tmp = min(tmp,abs(a-C)+abs(b-A)+abs(c-B))
        tmp = min(tmp,abs(a-C)+abs(b-B)+abs(c-A))
        if cnta>=2:
            tmp += (cnta-1)*10
        if cntb>=2:
            tmp += (cntb-1)*10
        if cntc>=2:
            tmp += (cntc-1)*10
        ans = min(ans,tmp)
print(ans)







