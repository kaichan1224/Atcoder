def INT(): return int(input())
def MAP(): return map(int,input().split())
def LIST(): return list(map(int,input().split()))
mod = 998244353
#--------------------------------------------------------------
N,M,K,S,T,X = MAP()
G = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = MAP()
    G[u].append(v)
    G[v].append(u)

dp = [[[0]*2 for _ in range(K+1)] for _ in range(N+1)]
dp[S][0][0] = 1
for k in range(K):#k回通る
    for now in range(1,N+1):#n頂点目に着目
        for nxt in G[now]:
            if nxt == X:
                dp[nxt][k+1][1] += dp[now][k][0] % mod
                dp[nxt][k+1][0] += dp[now][k][1] % mod
            else:
                dp[nxt][k+1][1] += dp[now][k][1] % mod
                dp[nxt][k+1][0] += dp[now][k][0] % mod
print(dp[T][K][0]%mod)
            