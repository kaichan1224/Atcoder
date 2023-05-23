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
6 7
1 2 5
1 4 4
2 3 4
2 5 7
3 6 3
4 5 3
5 6 5

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>

<キーワード>
・最大フロー、最小カットについて
フロー:ある場所からある場所まで運んだ荷物の量
・残余ネットワーク:あとフローをどれだけ追加でき、どれだけ戻すことができるかを重みつき有向グラフで著したもの
(逆向きにグラフを貼ればよい)
・フロ- a->b (3/8)あと5だけ流せる、3戻すことも可能
・残余ネットワーク a->b(5) b->a (3)

<ポイント>
最大フローのアルゴリズムについて
1.残余ネットワークでsからtまで辿れるような道を適当に見つけ、その道に流せるだけのフローを流す
2.その際に、残余ネットワークの辺の重みを書き換えるのを忘れないように
3.1,2を繰り返し、sからtまで流せる道がなくなった時のフローが最大フローになる

なぜこのアルゴリズムで成り立つか
->残余ネットワークを考えることにより、仮に、先に追加した増大道が邪魔したとしても
逆向きの辺(押し戻す部分)を張っていることにより、正しく最大フローを求められる。

・計算量について
DinicのアルゴリズムはO(M*N^2)
フォールドファーカーソンO(|最大フローf|*|M|)

<おまけ>
・無向グラフの時->双方向に辺を張る
・複数始点、複数終点がある時、新たな始点、終点を一つ用意してそれらにつなぐ
(このような考え方は重要,但し、始点と終点のペアが決まっているときはNP完全)
・最大流の答え=最小カットの値
・最小カットとは:頂点1からNまで到達できないようにするのに、最小で何円を使う必要があるか
"""
#--------------------------------------------------------------
from collections import deque
class FlowGraph:
    '''流量(フロー)を扱うグラフ
    実装済み：
        ・最大流1 flow1() O(|E||V|^2)
    '''
    def __init__(self, N):
        '''初期化 FlowGraph(頂点数)
        使い方:
            平面座標を扱うときは (i, j) → i * W + j 等で整数に変換する
        Args:
            N (int): 頂点数
        Returns:
            void
        '''
        self.n = N  # 頂点数
        self.edges = [[] for i in range(N)]  # 辺の情報
        self.pos = []  # 辺の番号 (From, edges[From]内の辺情報の位置)
    def addEdge(self, From, To, cap=1):
        '''辺の追加 addEdge(始点, 終点, 容量)
        Args:
            From (int): 始点の番号
            To (int): 終点の番号
            cap (int?): 辺の容量, 初期値 1
        Returns:
            int: 辺の番号
        '''
        assert 0 <= From < self.n
        assert 0 <= To < self.n
        assert 0 <= cap
        m = len(self.pos)
        self.pos.append((From, len(self.edges[From])))
        self.edges[From].append({'to':To, 'cap':cap, 'rev':len(self.edges[To])})
        self.edges[To].append({'to':From, 'cap':0, 'rev':len(self.edges[From])-1})
        return m

    def getEdge(self, i):
        '''辺情報の取得 getEdge(辺番号)
        Args:
            i (int): 辺の番号
        Returns:
            dict: 辺の情報 {'from':始点,
                            'to':終点,
                            'cap':容量,
                            'flow':流量}
        '''
        m = len(self.pos)
        assert 0 <= i < m
        e = self.edges[self.pos[i][0]][self.pos[i][1]]
        reve = self.edges[e['to']][e['rev']]
        return {'from':self.pos[i][0],
                'to':e['to'],
                'cap':e['cap'] + reve['cap'],
                'flow':reve['cap']}

    def getGraph(self):
        '''全ての辺の情報を取得
        Returns:
            list: i番目の辺のdict
        '''
        res = []
        for i in range(len(self.pos)):
            res.append(self.getEdge(i))
        return res

    def changeEdge(self, i, cap, flow):
        '''辺の流量を変更する changeEdge(辺番号, 新容量, 新流量)
        Args:
            i (int): 変更する辺の番号
            cap (int?): 変更後の容量
            flow (int?): 変更後の流量
        Returns:
            void
        '''
        m = len(self.pos)
        assert 0 <= i < m
        assert 0 <= flow <= cap
        e = self.edges[self.pos[i][0]][self.pos[i][1]]
        reve = self.edges[e['to']][e['rev']]
        e['cap'] = cap - flow
        reve['cap'] = flow

    def flow1(self, st, gl, flowlimit=(1<<63)-1):
        '''最大流を求める flow(始点, 終点, 流量の上限) O(|E||V|^2)
        Args:
            st (int): 始点の番号
            gl (int): 終点の番号
            flowlimit (int?): 流量の上限 初期値は64bit整数最大値
        Returns:
            int?: 最大の流量
        '''
        assert 0 <= st < self.n
        assert 0 <= gl < self.n
        dist = [0] * self.n  # stからの距離
        iter = [0] * self.n  #
        q = deque()

        def bfs():  # stからの距離を求めておく
            for i in range(self.n):
                dist[i] = -1
            dist[st] = 0
            q = deque()
            q.append(st)
            while q:
                now = q.popleft()
                for e in self.edges[now]:
                    if e['cap'] == 0 or dist[e['to']] >= 0:
                        continue
                    dist[e['to']] = dist[now] + 1
                    q.append(e['to'])

        def dfs(func, v, f):  # v → gl に流せる f
            if v == gl:
                return f
            while iter[v] < len(self.edges[v]):
                e = self.edges[v][iter[v]]
                if e['cap'] > 0 and dist[v] < dist[e['to']]:
                    d = func(func, e['to'], min(f, e['cap']))
                    if d > 0:
                        self.edges[v][iter[v]]['cap'] -= d
                        self.edges[e['to']][e['rev']]['cap'] += d
                        return d
                iter[v] += 1
            return 0

        flow = 0
        while flow < flowlimit:
            bfs()
            if dist[gl] < 0:
                return flow
            iter = [0] * self.n
            f = 0
            while True:
                f = dfs(dfs, st, flowlimit-flow)
                if f <= 0:
                    break
                flow += f
        return flow
    
    
N,M = MAP()
f = FlowGraph(N)
for _ in range(M):
    a,b,c = MAP()
    a,b = a-1,b-1
    f.addEdge(a,b,c)
print(f.flow1(0,N-1))