#プロコン
"""
高橋くんはプロコンに参加している。
高橋くんは３つの課題に取り組んだ。
課題ごとに配点が定められており、各課題ごとに1以上10以下の整数による評価がつけられる。
評価の数字がXであるとき、その課題において配点のX割の特典が与えられる。
３つの課題の配点と評価が与えれるので、高橋くんが合計何点得点したのか求めてほしい。
＃プロコンとは、グラフ状に適切にプロットする力を問うコンテストのこと
"""
a=int(input("課題1の配点を入力してください："))
b=int(input("課題2の配点を入力してください："))
c=int(input("課題3の配点を入力してください："))

d=int(input("高橋くんの課題1の点数を入力してください："))
e=int(input("高橋くんの課題2の点数を入力してください："))
f=int(input("高橋くんの課題3の点数を入力してください："))

print("高橋くんの合計得点は",a*(d/10)+b*(e/10)+c*(f/10),"点です。")