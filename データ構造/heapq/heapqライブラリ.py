'''
log(N)で最小値または最大値の追加・削除が可能
取り出す値が大きいとき10^9は取り出す行為を10^5するとしても
TLEしてしまうので注意!→工夫するとTLE取れるかも
'''
import heapq
class Heapq:
    #最大値を取り出したいときは、desc=Trueにする
    def __init__(self, arr, desc=True):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
    #最大or最小を取り出す
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
    #値を追加する
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
    #最大or最小を参照するだけ(なくならない)
    def top(self):
        return self.hq[0] * self.sign

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