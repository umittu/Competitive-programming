#入浴時間

N = int(input("入浴時間を入力（秒）；"))

H = N//3600
M = (N-H*3600)//60
S = N-(H*3600)-(M*60)

if N <= 86399:
    print(H,":",M,":",S)
else:
    print("ERROR")