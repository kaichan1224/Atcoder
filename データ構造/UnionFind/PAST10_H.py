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
5 7
1 1 2
2 2
1 3 4
2 5
1 1 4
2 1
2 4
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<問題要約>
N頂点クエリQ個
・1 u v : 頂点 u,v を結ぶ無向辺を追加する。
・2 u : クエリが与えられた時点でのグラフにおいて、頂点 u から 0 本以上の辺
を通ってたどり着くことのできる頂点の番号を全て昇順に出力する。

<考察>
・普通にBFSやるとO(N*Q)
・小さい順にグラフを繋いでみる?(有向グラフ)→結局オーダーは変わらない

<ポイント>
・マージテク(今は知らなくて良い)：集合をまとめる時に大きい方から小さい方を移動させることでマージさせると
計算量がならしO(logN)

↓マージテクは難しいがこんなこと考えなくてもよき

・uとvが同じ連結成分に属している場合は、その辺を追加する必要はない
→追加する辺を制限すると、グラフが常に森として保たれるため、サイズnの連結成分に含まれる
頂点をbfsにより列挙することができる

<注意>
・制約の見落としはだめ!!!!
→クエリで出力する頂点の番号の"合計"個数が2*10**5
.毎回長い配列を作るのは、計算量がかかるので注意!
→各クエリでNの配列を新しく作るのはNG!
→deque([now,pre])で扱う頂点数が少ないのでdist[N]を作るのはNG!
"""
#--------------------------------------------------------------
from typing import List
class UnionFind:
    """0-indexed"""
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n  # 辺がないとき、連結成分はn個あります

    def unite(self, x, y):
        """xとyをマージ"""
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return 0
        self.__group_count -= 1  # 木と木が合体するので、連結成分数が1減ります
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return self.parent[x]

    def is_same(self, x, y):
        """xとyが同じ連結成分か判定"""
        return self.root(x) == self.root(y)
    
    def members(self,x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]
        
    def root(self, x):
        """xの根を取得"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x):
        """xが属する連結成分のサイズを取得"""
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """全連結成分のサイズのリストを取得 O(N)"""
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """全連結成分の内容のリストを取得 O(N・α(N))"""
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())

    def group_count(self) -> int:
        """連結成分の数を取得 O(1)"""
        return self.__group_count  
    
N,Q = MAP()
uf = UnionFind(N)
G = [[] for _ in range(N)]
for _ in range(Q):
    que = LIST()
    if que[0]==1:
        u,v = que[1],que[2]
        u,v = u-1,v-1
        if uf.is_same(u,v)==False:
            uf.unite(u,v)
            G[u].append(v)
            G[v].append(u)
    else:
        u = que[1]
        u = u - 1
        que = deque([(u,-1)])
        ans = [u]
        while que:
            now,pre= que.popleft()
            for nxt in G[now]:
                if nxt != pre:
                    que.append((nxt,now))
                    ans.append(nxt)
        ans.sort()
        for i in ans:
            print(i+1,end=' ')
        print()
            
        
        
    