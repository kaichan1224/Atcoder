"""
全探索、計算量改善
x = N-f(x)
f(X)は0<=f(X)<=153なので,(N-153~N)の範囲で全探索すれば良い
上界外界を見積もる！！！！！
"""

N=int(input())
def calc(x):
    ANS=0
    for s in str(x):
        ANS+=int(s)
    return ANS

ANS=[]
for i in range(N-1000,N):
    if i<=0:
        continue
    if i+calc(i)==N:
        ANS.append(i)

print(len(ANS))
for a in ANS:
    print(a)