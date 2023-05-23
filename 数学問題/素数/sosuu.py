#１ 素数を判定する関数
def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

isprime(101)

#2
# 1 以上 N 以下の整数が素数かどうかを返す
def Eratosthenes(N):
    # テーブル
    isprime = [True] * (N+1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか
    return isprime

# 50 以下の素数をすべて求める
N = int(input())
isprime = Eratosthenes(N)
index = [i for i,x in enumerate(isprime) if x==True]
print(*index)