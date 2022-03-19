#勝率計算
"""
野球のAtCoderリーグのシーズンが終了した。チーム高橋はA試合中B回勝ち、チーム青木はC試合中D回勝ちました。
AtCoderリーグでは勝率の高い順に順位が与えられます。
チーム高橋とチーム青木ではどちらのチームが勝率で勝っているかを計算するプログラムを作成せよ。
・入力は以下の形式で与えられる。
A B C D
B=<A かつ D=<C
"""

A,B,C,D = map(int,input().split())

E = B/A
F = D/C
if E == F:
    print("DRAW")
elif E>=F:
    print("TAKAHASHI")
else:
    print("AOKI")