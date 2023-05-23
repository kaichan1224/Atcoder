#配列用二分探索
import bisect
a=[1,2,2,2,3]
#一致する要素のうち(もしかぶっていたら)左のindex出力
bisect.bisect_left(a,2)
#一致する要素のうち(もしかぶっていたら)右のindex出力
bisect.bisect_right(a,2)

#めぐる式二分探索
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok