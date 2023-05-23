import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
1
3
"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<期待値DPのコツ>
https://compro.tsutaj.com//archive/180220_probability_dp.pdf で+1する意味を理解しよう!!!!
回数の期待値DPの形
・dp[i] =(dp[何か]+(回数))*(確率)+(dp[何か]+(回数))*(確率)+...
・dp[i] = (dp[何か])*(確率)+(dp[何か])*(確率)+...+1 でもいい(?)
・Nターンあったら、各ターンは別々に期待値が計算できたりする
・状態遷移を表すグラフを作ることができれば、期待値についての立式をすることができる

- 持つべき状態を見極めろ!!!!
- 状態から状態への遷移はどうなるか

<考察>
dp[i]:皿が残りi個の時の期待値
とる時と取らない時があるのに注意

<ポイント>
dp[a][b][c]:寿司が残り1,2,3個の皿の個数
dp[0][0][0]が答え
dp[a][b][c] = dp[a-1][b][c]*(a/N)+dp[a+1][b-1][c]*(b/N)+dp[a][b+1][c-1]*(c/N)+dp[a][b][c]*((N-a-b-c)/N)+1 

dp[a][b][c](1-(N-a-b-c)/N) = (移項後右辺)
わって終わり
・コーナーケースに気をつける必要があるので、それぞれ分割
・割り算するときもそれぞれに割ってあげた方が良さげ
・配列のサイズを大きめに取ろうねというお話
→というか、b+1,a+1を見る場面があるので大きめに取っておかなければならない.
"""
#-------------------------------
N = INT()
A = LIST()
a = 0
b = 0
c = 0
for item in A:
    if item==1:
        a += 1
    elif item==2:
        b += 1
    else:
        c += 1
dp = [[[-1]*(300+1) for _ in range(300+1)] for _ in range(300+1)]
def memo(a,b,c):
    if dp[a][b][c]!=-1:
        return dp[a][b][c]
    if a==0 and b==0 and c==0:
        dp[0][0][0] = 0
        return 0
    res = 0
    abc = a+b+c
    tmp = 1-(N-abc)/N
    res += 1/tmp
    if a>0:
        res += ((memo(a-1,b,c))*(a/N))/tmp
    if b>0:
        res += (memo(a+1,b-1,c))*(b/N)/tmp
    if c>0: 
        res += (memo(a,b+1,c-1))*(c/N)/tmp
    dp[a][b][c] = res
    return dp[a][b][c]

ans = memo(a,b,c)
print(ans)






