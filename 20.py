#高橋くんと年齢
"""
高橋くんは年齢を忘れてしまいました。
ひとまず３人の友達を集めることに成功したので、その３人が予想する高橋くんの年齢の中央値を、高橋くんの年齢として代用することにしました。
高橋くんに代わって３つの整数a,b,cから中央値を求めるプログラムを作成しなさい。
"""
import statistics

a,b,c = map(int,input().split())

l = [a,b,c]

median = statistics.median(l)

print("高橋くんの予想年齢は",median,"です。")