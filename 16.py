#高橋くんの研修
"""
高橋くんはソフトウェア会社に勤めています。その会社では、短い変数名はバグを生む原因だと信じられており、長い変数を使う習慣があります。
いま高橋くんは２つの変数名を思いつきましたが、残念なことにその長さを見分けることができません。
いろいろな意味でかわいそうな彼の代わりに、与えられた２つの小文字アルファベットのみからなる文字列のうち、文字列が長い方の文字列を求めてください。
"""

a=input("１つ目の変数名を入力してください：")
b=input("２つ目の変数名を入力してください：")

if len(a)>len(b):
    print(a)
else:
    print(b)