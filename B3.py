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


s = list(input())
t = list(input())

r = ['a','t','c','o','d','e','r']

for i in range(len(s)):
    if s[i] == '@' and t[i] in r:
        t[i] = '@'
    elif t[i] == '@' and s[i] in r:
        s[i] = '@'

if s == t:
    print("You can win")
else:
    print("You will lose")
        