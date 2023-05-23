"""
*与えられた有向グラフに対し、各頂点を辺の向きに沿うように順序付けて並び替えること
*dfsにおける再帰関数を抜けた順番に頂点を並べ、逆順に並び直す
*計算量(|V|+|E|)
*DPの更新の順序が分かる、DAGの最短経路はDPで。
"""
#DAGの有向パスのうち最長のもの
#length[i]:iを始点とするバスのうち、最も長いものの長さ
def topologicalsort(N, G):
    import heapq
    in_number = [0] * N #各頂点の枝の本数をカウントするためのリストを用意する
    for i in G:
        for v in i:
            in_number[v] += 1 #頂点vの入次数をカウントする
    S = [] #手順1:空のリストを用意する。
    queue = [i for i in range(N) if in_number[i] == 0] #入次数が0の頂点を記録するためのリストを用意
    heapq.heapify(queue) # リストを優先度付きキューへ
    while queue:
        u = heapq.heappop(queue) #手順2.1：入次数が0の頂点でかつ最小の頂点uを取り出す
        S.append(u) #手順2.2：手順1で作ったリストSに追加しています。
        for u2 in G[u]:
            in_number[u2] -= 1 #手順2.3：uから出ている辺（枝）を削除
            if in_number[u2] == 0: #uから出ている辺を削除していく作業で頂点u2の入次数が0となった場合
                heapq.heappush(queue, u2) #u2はuの候補となる
    return S