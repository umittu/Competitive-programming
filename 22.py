#足し算
"""
正整数Nと、２の累乗数1,2,4,8があります。
これらのうち、同じ２の累乗数をいくつ使っても良いので、それらの和がNとなるような組み合わせを一つ求めでください。
これらの組み合わせが複数考えられる場合は、そのうちどれを出力しても構わない。
"""

N=int(input("正整数Nを入力してください："))

list_ans=[]

while N>0:
    if N>=8:
        list_ans.append(8)
        N=N-8
    elif 8>N>=4:
        list_ans.append(4)
        N=N-4
    elif 4>N>=2:
        list_ans.append(2)
        N=N-2
    else:
        list_ans.append(1)
        N=N-1
print(list_ans)

