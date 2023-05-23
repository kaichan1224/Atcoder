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
        #return {'from':self.pos[i][0],'to':e['to'],'cap':e['cap'] + reve['cap'],'flow':reve['cap']}
        return reve['cap']

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
#--------------------------------------------------------------
_INPUT = """\
10 2
101001000011000100010111
000010011110110010100111
101110001110000011110111
011011110100011110100011
000011001111111010110001
001010011010101010110100
001010010111101101111010
110011111100010110111011
100010011100011101110001
010110100101101111111011


"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・どの時間帯にもM人以上が勤務して、かつ、10時間までそれぞれ働くことができる場合
それが実現可能か。

<キーワード>
・二部マッチング

<二部マッチングを使うと知ってうえでさらに考察>
・N人が0~23にマッチングするかどうか
(start)->{0,1,...,N-1}->{N,N+1,N+23}->終点
・1日10時間までしか勤務することができないという部分をどのように解消するか->最大容量10の辺をクッションに挟む?

・一人当たり10時間までしか働くことができない
開始->0~Nの流量を10(最大値にする),
・どの時間帯にもM人以上が勤務している必要がある(流量の最大値をMにして全ての時間帯の辺についてその条件を満たすかどうかを見る)

AC(実質)
・最大流がM*24の時のみ条件を満たしている

<ポイント>
・辺の重さを工夫してやる(制限の部分をうまく処理する)
"""
#--------------------------------------------------------------
N,M = MAP()
C = [list(input()) for _ in range(N)]
dinic = FlowGraph(N+26)
#0~N-1人,N~N+23時間,スタートN+24,ゴールN+25
cnt = [0]*N
for i in range(N):
    for j in range(24):
        if C[i][j]=="1":
            cnt[i] += 1
for i in range(N):
    dinic.addEdge(N+24,i,min(cnt[i],10))#それぞれの最大流量(min(10,C[i][0~23]で1の個数:))にしたほうがいいかも
for i in range(N,N+24):
    dinic.addEdge(i,N+25,M)#M人通れば良い

for i in range(N):
    for j in range(24):
        if C[i][j]=="1":#働ける時
            dinic.addEdge(i,N+j,1)
ans = dinic.flow1(N+24,N+25)
if ans == 24*M:
    print("Yes")
else:
    print("No")
"""
flag = True
for i in range(N,N+24):
    if dinic.getEdge(i)!=M:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
"""




