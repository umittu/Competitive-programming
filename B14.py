#価格の計算
"""
#商品数(n)の入力
n = int(input("商品数を入力；"))
#部分集合の(X)入力
X = int(input("商品の部分集合くを入力；"))
#部分集合(X)を2進数に変換
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

Y = (base10int(X, 2))

Z = str(Y)
if len(Z) != n:
    W = '0'+Z 
else:
    W = Z

print(W)
諦めた
"""
