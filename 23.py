#BestBody
"""
高橋くんは太りやすく痩せやすい体質です。そこで彼はN日間の体重の変化量を記録してみました。
１日目の高橋くんの体重はWキログラムでした。i日目(2<=i=<N)の体重変化量はAi キログラム（負）でした。
つまりi-1日目の体重をXキログラムとすると、i日目の体重はX+Aiキログラムだったということになる。
ところで、高橋くんの個人的な価値観では、体重がSキログラム以上Tキログラム以下の体型が「ベストボディー」だと考えています。
体重を記録したN日間のうち、高橋くんがベストボディーであった日数を求めてください。
"""

n=int(input("体重を記録した日数を入力してください："))
s=int(input("ベストボディーの下限体重を入力してください"))
t=int(input("ベストボディーの上限体重を入力してください："))
x=int(input("１日目の高橋くんの体重を入力してください："))

list_weight=[]

for i in range(n):
    a=int(input("i日目の体重を入力してください："))
    list_weight.append(a)
    a=a+1

print(list_weight)
