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
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・構築問題
h,wともに<=100のグリッドを作成。
白で塗られたマスの集合はA個の連結成分に分かれ、黒で塗られたマスの集合はB個(略)
最高10000のマスの中で、連結成分が最大500,500個ずつできるように色塗りをしなければならない
<キーワード>
・構築問題
・発想が必要

<ポイント>
条件を満たすグリッドは以下のようにして構成することができます。
• K = 50 として、2Kx2K のグリッドを用意する。
• 上から K 行以内にあるマスを全て黒く塗り、残りのマスをすべて白く塗る。
• 上から K-1 行以内のマスのうち A-1 個のマスを上下左右斜めに隣り合わないように選び、それら
の色を白に変える。
• 下から K-1 行以内のマスのうち B-1 個のマスを上下左右斜めに隣り合わないように選び、それら
の色を黒に変える。
"""
#--------------------------------------------------------------
A,B = MAP()
