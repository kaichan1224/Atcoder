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
11 4
1 2 3 6
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・貪欲に大きい値を取るのはだめ
・minimax法?
-DPで解けそうだけど遷移がわかんない

<キーワード>
・dp[i] = max(dp[i],i-dp[i-A[j]])この遷移を書けるかどうかが全て。


<ポイント>
・逆戻りしてくタイプのDP(伝われ)
・高橋君がAj個取った時、青木君は(高橋が残っている石の数-Aj個)残っている状態になる
・この状態で青木君はdpA[i-A[j]]個最大で取ることができるため、高橋君が
高橋君が残っている石の数-dpA[i-A[j]]個分取ることができる。
(青木君が持っている数の最大値+高橋君が持っている数の最大=その時点での石の数)
を式変形すると、高橋君が持っている数の最大値=その時点での石の数-青木君が持っている数の最大値
となり、高橋君が石iこ取ることができる状態での最大値は、Aj個高橋君が取った時、

・実はDP配列ひとつで溶けたりするが、その判断をするのはなかなか難しいので、やりたいことを
着実に実装していくのが理想。

"""
#--------------------------------------------------------------
N,K = MAP()
A = LIST()
dpT = [-1]*(N+1)#石がN個残っている時に高橋君が取ることができる石の個数の最大値
dpA = [-1]*(N+1)#~青木君~
#別枠で実験~
dp = [-1]*(N+1)
dp[0] = 0

#もう少しわかりやすく書くと、石がn個残っている時のそれぞれが取れる最大の点数
dpT[0] = 0
dpA[0] = 0



for i in range(1,N+1):#i個残っている時に
    for j in range(K):#K番目の石をとる
        if i-A[j]<0:
            break
        #高橋君が取ることができる枚数は,石がi個残っている時の青木君が取ることができる石の数(確定)
        #高橋君がAj個の石を取った時、最終的に取れる石の個数は、
        
        #石がi-Aj個残っている状態からゲームを始めた時の相手が取ることのできる石の個数
        dpT[i] = max(dpA[i],i-dpA[i-A[j]])
        dpA[i] = max(dpT[i],i-dpT[i-A[j]])
        
        dp[i] = max(dp[i],i-dp[i-A[j]])
        #print(dpT,dpA)
print(dp[N])
#print(dpT[N])

        
    
