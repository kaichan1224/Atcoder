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
abcdefghijklmnopqrstuvwzyx
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
*Sの一番うしろから見る
*Sの長さが26じゃないときは文字を付け足して最小のものをつかえばよい
*Sの長さが26のときは、後ろから見て辞書順が次に大きいものを探す
*usedリストが必要

"""
#--------------------------------------------------------------
S = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
d = defaultdict(int)
for a in alp:
    d[a] = 0
for s in S:
    d[s] += 1
if len(S)!=26:
    for k,i in d.items():
        if i==0:
            print(S+k)
            exit()
else:
    flag = False
    for i in range(26)[::-1]:
        if S[i]!=alp[i]:
            tmp = S[i] #入れ替えるべき文字
            index = i
            flag = True
            break
    if flag==False:
        print(-1)
        exit()
    ans = ''
    for i in range(26):#入れ替え前のもじを探す
        if S[i]==alp[index]:
            t = i #tここまで使う
    for i in range(t):
        ans += S[i]
    ans += tmp
    print(ans)










