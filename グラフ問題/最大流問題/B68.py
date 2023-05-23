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
#--------------------------------------------------------------
_INPUT = """\
5 2
3 4 -1 -5 5
1 3
2 4

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
"""
<考察>
・N個の駅のうち0個以上を特急駅に指定->指定しなくても良い?(嘘)
・M個の提案全ての守る必要がある
全て守った場合の利益?

<最大流・最小カットについて再掲>
・最大フロー、最小カットについて
フロー:ある場所からある場所まで運んだ荷物の量
・残余ネットワーク:あとフローをどれだけ追加でき、どれだけ戻すことができるかを重みつき有向グラフで著したもの
(逆向きにグラフを貼ればよい)
・フロ- a->b (3/8)あと5だけ流せる、3戻すことも可能
・残余ネットワーク a->b(5) b->a (3)

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

その他
・無向グラフの時->双方向に辺を張る
・複数始点、複数終点がある時、新たな始点、終点を一つ用意してそれらにつなぐ
(このような考え方は重要,但し、始点と終点のペアが決まっているときはNP完全)
・最大流の答え=最小カットの値
・最小カットとは:頂点1からNまで到達できないようにするのに、最小で何円を使う必要があるか

<キーワード>
燃やす埋める問題の定義について(複数掲示)
1.複数の小問題に対して選択肢とコスト・報酬が与えられて、選択肢同士に依存関係があるような問題
2.
-複数の小問題がある(それぞれの小問題に対し選択肢があり、選択肢ごとに費用・利益がありうる)
-選択肢同士に依存関係もありうる
-全体の費用を最小化する(利益を最大化)

<ポイント>
・燃やす埋める問題
-選択肢間の依存関係については、新しくコスト無限大の辺の追加して調整
-燃やす操作をスタートs,埋める操作をゴールtと仮定し、
それぞれの操作に対するコストを1~Nに対応する部分に対して辺を張る

<仕組みのお話>(https://www.slideshare.net/shindannin/project-selection-problem)
-基本的には、金額の安い選択肢を選べば良い。
例として,A,B,Cさんが燃やす、埋めるの操作を行えることを考える.
埋める操作をs,燃やす操作をtとし、小問題ごとに並列につなげる(s->{A,B,C}->t)
-この最小s-tカットを考えると、これが小問題の答えとなる(最小カット=最大流より、実際には最大流を求めれば良い)

<問題パターン>
1.燃やす埋めるのコストの最小値を求めたい時
->そのまま辺を張って最小カット(=最大流)を求めれば良い
2.燃やす埋めるのコスト(利益)の最大値を求めたい
->最小カットでは最小値しか求めることができないので、最小値問題へ置き換える必要がある
->利益が大きい選択肢の値を無条件で得られることにし、その分を選択肢から引くことで全て損失に置き換えることができる
(この時、損失の値が負になってしまうとこれはNP困難なためダメ)
->コスト0の辺もグラフに書く

+制約追加
3.頑張る、コストが負になる可能性があり、かつ、相手側の操作がコスト0の場合は反対側のコストに移動すれば良い

これらを踏まえた上で
<考察>
・埋める:特急駅に指定しない(利益Pi円) 燃やす:特急駅に指定する(利益0円)
・またM個の依存関係が存在する
・最大の利益を求めたい=最小のコストと置き換えて、最小カットを考える
・負辺が存在しないようにする必要がある
ー>コストが負になる場合は、逆の操作側の方にコストとして辺を張ることで解消
(指定しない時の利益は0だから)
・aとbに依存関係がある(a->bだけど,b->aではないことに注意する)
・利益をコストと捉えて最小コストを求め、その後全体の利益-最小コストが最大の利益

・依存関係の辺をどのように貼れば良いのかについて
(指定しない)->{1~N}->(指定する)
"""
#--------------------------------------------------------------
N,M = MAP()
P = [0]+LIST()
dinic = FlowGraph(N+2)
#特急駅駅に指定しない=埋める(頂点0)、指定する=燃やす(頂点N+1)としてグラフを張っていく
#最大の利益を求めたいので、最小値問題に置き換える必要がある
for i in range(1,N+1):
    if P[i]>=0:
        dinic.addEdge(0,i,P[i])
        dinic.addEdge(i,N+1,0)
    else:
        dinic.addEdge(0,i,0)
        dinic.addEdge(i,N+1,abs(P[i]))
       
for _ in range(M):
    a,b = MAP()
    dinic.addEdge(a,b,INF)#どっちが正しいか要チェックa->bのコストは無限(つまりカットは実質不可能)

ans = dinic.flow1(0,N+1)
tmp = 0
for p in P:
    if p>=0:
        tmp += p
print(tmp-ans)
    
