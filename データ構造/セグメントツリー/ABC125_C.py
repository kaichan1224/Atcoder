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
#mod = 10**9+7
#mod = 998244353
######################################################
_INPUT = """\
3
12 15 18
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
セグメントツリーを使って計算
実現できる最大公約数の最大値はA[i]以外の最大公約数となること
に気がつくことができたら、後はセグ木で殴るだけ。
"""
######################################################
def segfunc(x,y):
    '''
    区間の
    和→x+y
    差→x-y
    最小値→min(x,y)
    xor→x^y
    or→x|y
    最大公約数→math.gcd(x,y)
    '''
    return math.gcd(x,y)

class SegTree:
    '''
    セグメントツリーの構築は
    seg = SegTree(元のリスト、単位元、segfunc)
    単位元：どの数に対して演算を行っても元から変わることがない数
    和:0
    積:1
    or:0
    xor:0
    最大公約数:0
    最小値：大きな数 inf
    最大値：小さな数 -inf
    select(インデックス番号):値の参照 O(1)
    update(インデックス番号、値):値の更新O(logN)
    query(左端インデックス番号、右端インデックス番号):指定区間についての演算結果を返すO(logN)
    '''
    def __init__(self,x_list,init,segfunc):
        self.init=init
        self.segfunc=segfunc
        self.Height=len(x_list).bit_length()+1
        self.Tree=[init]*(2**self.Height)
        self.num=2**(self.Height-1)
        for i in range(len(x_list)):
            self.Tree[2**(self.Height-1)+i]=x_list[i]
        for i in range(2**(self.Height-1)-1,0,-1):
            self.Tree[i]=segfunc(self.Tree[2*i],self.Tree[2*i+1])

    def select(self,k):
        return self.Tree[k+self.num]

    def update(self,k,x):
        i=k+self.num
        self.Tree[i]=x
        while i>1:
            if i%2==0:
                self.Tree[i//2]=self.segfunc(self.Tree[i],self.Tree[i+1])
            else:
                self.Tree[i//2]=self.segfunc(self.Tree[i-1],self.Tree[i])
            i//=2

    def query(self,l,r):
        result=self.init
        l+=self.num
        r+=self.num+1

        while l<r:
            if l%2==1:
                result=self.segfunc(result,self.Tree[l])
                l+=1
            if r%2==1:
                result=self.segfunc(result,self.Tree[r-1])
            l//=2
            r//=2
        return result
N = INT()
A = LIST()
#その点を除く最大公約数の最大値
seg = SegTree(A,0,segfunc)
ans = 1
for i in range(N):
    if i==0:
        tmp = seg.query(1,N-1)
    elif i==N-1:
        tmp = seg.query(0,N-2)
    else:
        a = seg.query(0,i-1)
        b = seg.query(i+1,N-1)
        tmp = math.gcd(a,b)
    ans = max(ans,tmp)
print(ans)