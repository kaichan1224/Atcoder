import io
import sys
from collections import deque,defaultdict
from heapq import heappush,heappop 
import heapq
from itertools import product,combinations,accumulate
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
_INPUT = """\
6 4 3
3 1 4 1 5 9




"""
sys.stdin = io.StringIO(_INPUT)
#-------------------------------
"""
<考察>
昇順のk個の和を求める問題
・なくなるカードがK番目よりも低い順位だったら結果に影響なし
・そうでなければ引く必要がある???
・削除追加する時のindex管理を丁寧にする必要がありそう??

<ポイント>
・M個の要素のうち、上位K個以上かそうでないかで分けて考えたら楽に出来そう。
・上位K個に含まれたらA,そうでなければBと分けてデータを持つことを考えてみる
↓
ヒープ二本使えば管理できそう。

<double heap>
・最大と最初両方考えるのがめんどくさい人用のどっちも使えるheap
"""
#-------------------------------
class DoubleHeap:
    def __init__(self):
        self.minh = []
        self.maxh = []
        self.d = dict()
        self.size = 0
        self.total = 0
 
    def push(self, x):
        self.size += 1
        self.total += x
        heapq.heappush(self.minh, x)
        heapq.heappush(self.maxh, -x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1
 
    def get_min(self):
        return self.minh[0]
 
    def get_max(self):
        return -self.maxh[0]
 
    def pop_min(self):
        n = self.get_min()
        self.discard(n)
        return n
 
    def pop_max(self):
        n = self.get_max()
        self.discard(n)
        return n
 
    #消したかどうかの判定付き
    def discard(self, x):
        if x not in self.d:
            return False
        self.size -= 1
        self.total -= x
        self.d[x] -= 1
        if self.d[x] == 0:
            del self.d[x]
 
        while len(self.minh) != 0 and self.minh[0] not in self.d:
            heapq.heappop(self.minh)
        while len(self.maxh) != 0 and -self.maxh[0] not in self.d:
            heapq.heappop(self.maxh)
        return True
 
    def erase(self, x, n=10 ** 18):
        if x not in self.d:
            return 0
        if self.d[x] < n:
            n = self.d[x]
        self.size -= n
        self.total -= x * n
        self.d[x] -= n
        if self.d[x] == 0:
            del self.d[x]
 
        while len(self.minh) != 0 and self.minh[0] not in self.d:
            heapq.heappop(self.minh)
        while len(self.maxh) != 0 and -self.maxh[0] not in self.d:
            heapq.heappop(self.maxh)
        return n
 
    def is_exist(self, x):
        if x in self.d:
            return True
        else:
            return False
 
    def __len__(self, x):
        return self.size
 
    def len(self):
        return self.size
 
    def types(self):
        return len(self.d)
 
    def sum(self):
        return self.total

N,M,K = MAP()
A = LIST()
R = DoubleHeap()#上位K位(小さい順で)
L = DoubleHeap()#それ以外(それ以外)
tmp = A[:M]
tmpsort = sorted(tmp)
ans = []
#小さい順でK位とそうでないものでR,Lに分ける
for i in range(M):
    if i<K:
        R.push(tmpsort[i])
    else:
        L.push(tmpsort[i])
ans.append(R.sum())
#注意:Rには常にK個ある状態にしておかなければならない
for i in range(N-M):
    #追加する操作
    delnum = A[i]
    addnum = A[i+M]
    #まずLに追加、はみ出たのをtに移動する
    L.push(addnum)
    R.push(L.pop_min())
    L.push(R.pop_max())
    #次に消す操作
    if R.discard(delnum):
        R.push(L.pop_min())
    else:
        L.discard(delnum)
    ans.append(R.sum())
print(*ans)
        


    





