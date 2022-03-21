#価格の計算
n,x = map(int,input().split())
a = list(map(int,input().split()))
y = 0 
for i in range(n):
    if x >> i & 1: ans +=a[i]
print(y)
