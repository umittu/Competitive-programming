#AtCoderトランプ
"""
AtCoder社では1人で行うトランプを使ったゲームが流行っています。
AtCoder社特製のトランプでは、各カードにアルファベット小文字1文字、または@の文字が書かれています。
ゲームは以下の手順で行われます。
1.カードを同じ枚数ずつ2列に並べて文字列を2つ作ります。
2.@のカードは、それぞれa,t,c,o,d,e,rのどれかのカードと置き換えます
3.2つの列が指し示す文字列が同じであれば勝ち、同じでなければ負けです。
手順1.で並べられた2つの列が指し示す2つの文字列が与えられるので、適切に@に置き換えて、このゲームに勝つことができるかを判定するプログラムを書いてください。
"""
S,T = map(str,input().split())


for i in range(len(S)):
    if S[i] == '@' and T[i] == 'a':
        S[i].replace(S[i],'a')
    elif S[i] == '@' and T[i] == 't':
        S[i] == 't'
    elif S[i] == '@' and T[i] == 'c':
        S[i] == 'c'
    elif S[i] == '@' and T[i] == 'o':
        S[i] == 'o'
    elif S[i] == '@' and T[i] == 'd':
        S[i] == 'd'
    elif S[i] == '@' and T[i] == 'e':
        S[i] == 'e'
    elif S[i] == '@' and T[i] == 'r':
        S[i] == 'r'

print(S)
print(T)

if S == T:
    print("You will win")
else:
    print("You will lose")
        
