#seam carving関数
def seam_carving(arr) :
    print(a)
    #arr は入力画像
    #arrは重要度画像
    #2枚とも縮める必要がある
    #TODO ここを書き換える
    #STEP1:DPテーブル用意(総和最小を求めたいのでinfで初期化)
    dp = [[float("inf")]*arr.shape[1] for _ in range(arr.shape[0])]
    #STEP2:DPの初期化(一列目をそのまま持ってくる)
    for x in range(arr.shape[1]):
        dp[0][x] = arr[0,x]
    #STEP3:DP遷移する(もらうDP)
    for y in range(1,arr.shape[0]):
        for x in range(arr.shape[1]):
            if x==0:#左端
                dp[y][x] = min(dp[y-1][x]+arr[y,x],dp[y-1][x+1]+arr[y,x])
            elif x==arr.shape[1]-1:#右端
                dp[y][x] = min(dp[y-1][x]+arr[y,x],dp[y-1][x-1]+arr[y,x])
            else:
                dp[y][x] = min(dp[y-1][x]+arr[y,x],dp[y-1][x-1]+arr[y,x],dp[y-1][x+1]+arr[y,x])
    #STEP4:H行目の総和が最小の画素の位置を求める
    print()
    print(np.array(dp))
    tmpmin = float("inf")
    nowY = arr.shape[0]-1
    nowX = 0
    for x in range(arr.shape[1]):
        if tmpmin > dp[arr.shape[0]-1][x]:
            tmpmin = dp[arr.shape[0]-1][x]
            nowX = x
    #STEP5:DP復元
    ans = [nowX]
    while nowY>0:
        for dx in range(-1,2):
            if not (0<= nowX+dx < arr.shape[1]):
                continue
            if dp[nowY][nowX] == dp[nowY-1][nowX+dx] + arr[nowY,nowX]:
                nowY -= 1
                nowX += dx
                ans.append(nowX)
                break
    ans.reverse()
    print(ans)
    #STEP6:削除
    for y in range(arr.shape[0]):
        nowx = ans[y]
        t2 = arr[y,0]
        arr[y,0] = arr[y,nowx]
        for i in range(1,nowx)[::-1]:
            arr[y,i+1] = a[y,i]
        arr[y,1] = t2
    arr = arr[:,1:]
    print(arr)
