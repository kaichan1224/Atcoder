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
dirc = [(0,1),(0,-1),(1,0),(-1,0)]
#dirc2 = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
期待値について:一回の試行で得られる平均的な値
*期待値の線形性
→確率変数X1,X2,,Xnがあったとき、
(X1の期待値)+,,+(Xnの期待値)=(X1+,,+Xn)の期待値

* 有効なものが来るまでにカードを引く期待値は、
有効なカードを引く確率の逆数

* 状態の遷移は、連結数1→2→3,,,→N
それぞれの遷移を考えると(N-1)/Nの確率で次の遷移に映る(期待値逆数)

*全体でn個ある頂点からまだ訪れていない頂点n-iを訪れる確率は
(n-i)/nその期待値はn/(n-i)
https://kajindowsxp.com/abc194d/

* すべて同じ遷移条件であるためどこと連結化は抽象化して良い条件
* 状態の遷移にかかる回数の期待値を考える(連結数1→連結数2→...→連結数N) 
"""
######################################################
N = INT()
ans = 0
for i in range(1,N)[::-1]:
    #期待値の線形性、確率の逆数
    ans += N/(N-i)
print(ans)


