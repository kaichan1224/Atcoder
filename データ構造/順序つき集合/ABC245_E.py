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
2 3
2 4
3 2
8 1 5
2 10 5
"""
sys.stdin = io.StringIO(_INPUT)
######################################################
"""
考察
*縦幅が小さい順でチョコレートを一枚目から見る
*a以上のもので一番小さいc and b以上で一番小さいdの条件を満たすもの
が最後まで存在し続ければYes


→チョコと箱をまとめ管理する(縦、横、0 or 1(チョコまたは箱かを管理))
チョコと箱をまとめて縦の長さの降順にソート
→新たな配列を用意し、片方だけ見る

空の数列を用意し要素を前からみて、見ている要素が箱ならSにDを追加、
チョコならSの要素で横幅以上のものを削除する
もし削除できなければNo
"""
######################################################
import データ構造.順序つき集合.lib as lib
N,M = MAP()
A = LIST()
B = LIST()
C = LIST()
D = LIST()
box = []
for i in range(N):
    #縦、横、flag 0:チョコ 1:箱
    box.append((A[i],B[i],0))
for i in range(M):
    box.append((C[i],D[i],1))
box.sort(reverse=True)
print(box)
check = lib.SortedMultiset()
for y,x,flag in box:
    print(check)
    if flag==1:
        check.add(x)
    else:
        tmp = check.ge(x)
        if tmp==None:
            print('No')
            exit()
        check.discard(tmp)
print('Yes')
        



