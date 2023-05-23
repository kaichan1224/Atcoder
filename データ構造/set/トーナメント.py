import io
import sys
#sys.setrecursionlimit(10**7)
from collections import deque,defaultdict
from heapq import heappush,heappop 
import copy
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
"""
<考察>
・全員のプレイヤー名が異なる

<ポイント>
・優勝だけ知るなら簡単。なぜなら、以下の理由より。
・N-1回の試合のうち、優勝者を除くN-1名は一回だけ負けている
→負けたことのない人が答え
・余事象的な考え方

<注意(アホ)>
・入力を受け取る時に、複数行データをinput().split()で受け取る時に数値データを
文字型から数値型へ直すのを忘れないように!!!!!
"""
#--------------------------------------------------------------
N = INT()
name_list = set()
lose_list = set()
for _ in range(N-1):
    a,a_score,_,b_score,b = input().split()
    a_score,b_score = int(a_score),int(b_score)
    name_list.add(a)
    name_list.add(b)
    if a_score>b_score:
        lose_list.add(b)
    else:
        lose_list.add(a)
ans = name_list - lose_list
print(*ans)


            
    