#世界のFizzBuzz
print("数字Nが与えられます。Nに3が含まれる、もしくは3で割り切れる場合はYesを、それ以外の場合はNoと出力してください。")

N=int(input("任意の数字を入力してください："))

if N % 3 == 0 or "3":
    print("Yes")
else:
    print("No")