#高橋くんの集計
import math
n = int(input())
a = list(map(int,input().split()))
#リストの要素の合計値を出す
for i in range(n):
    if a[i] == 0:
        n -= 1
#バグの平均値を出す。
ans = sum(a)/n
print(math.ceil(ans))
