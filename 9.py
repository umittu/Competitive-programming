"""
高橋くんは子供の頃の写真を整理している。整理している最中に、写真を入れている木箱が出てきたので、木箱内にある写真をアルバムに貼って整理することにした。
どのくらいの大きさのアルバムが必要なのか確認するために、木箱内にある写真の枚数が知りたくなった。
高橋くんはすべての写真に正整数の通し番号をつけており、木箱内には通し番号がS以上T以下であるすべての写真が入っている。
高橋くんは、木箱内にある写真の枚数が知りたいが、写真を一枚づつ数えるのは大変である。
あなたは高橋くんの代わりに、SとTの値からアルバムに貼られている写真の枚数を計算するプログラムを作成せよ。
"""

s=int(input("小さい方の通し番号の値を入力してください："))
t=int(input("大きい方の通し番号の値を入力してください："))

print("高橋くんの木箱の中の写真の枚数は",t-s+1,"枚です。")