#１２月６日
"""
１２月６日は、月を日で割って割り切れる日です。日付が与えられるので月が日で割り切れるか判定してください。
"""
m=int(input("月を入力してください："))
d=int(input("日を入力してください："))

if m%d==0:
    print("Yes")
else:
    print("No")
