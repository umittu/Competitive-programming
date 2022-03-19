#25個の文字列
"""
高橋くんは短めの呼び名を考えています。呼び名は半角小文字アルファベット2文字で構成されます。
高橋くんには好きな5種類のアルファベットがあります。高橋くんは、以下の条件を満たす長さ2の文字列全てを考え、それらの集合を呼び名集合と呼ぶことにします。
・条件:文字列の1文字目も2文字目も高橋くんが好きな5種類のアルファベットのいずれかである。
ここで2つの長さ2の異なる文字列S,Tに関して、SがTよりも辞書順で前に来るというのは、以下の条件のうちいずれかが満たされたときです。
・文字列Sの1文字目と文字列Tの1文字目が異なり、かつ文字列Sの1文字目が文字列Tの1文字目よりもアルファベット順(ABC順)で先である。
・文字列Sの1文字目と文字列Tの1文字目が同じで、かつ文字列Sの2文字目が文字列Tの2文字目よりもアルファベト順で先である。
「呼び名候補の集合」を構成する文字列は全部で25個あります。高橋くんはそれらの文字列を辞書順に並べたときに先頭からN番目となる文字列を最終的な呼び名にすることにしました。
あなたの課題は高橋くんが定めた最終的な呼び名を求めることです。
"""
import itertools

A = list(itertools.product(input(),repeat=2))
A.sort()
index = int(input())-1

print("".join(A[index]))
