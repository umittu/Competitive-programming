#錠

a = int(input("現在のディスプレイ上の数字；"))
b = int(input("設定した数字；"))

#0<=(a,b)<=9
#即解錠
if a == b:
    print(0)

#赤いボタンを押す場合x
#青いボタンを押す場合y
if a < b:
    x = b-a
    y = 10+a-b
    print(min(x,y))
else:
    x = 10+b-a
    y = a-b
    print(min(x,y))

