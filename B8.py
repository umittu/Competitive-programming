#投票
import collections
N = int(input("組織の人数を入力してください；"))
list = []
for i in range(N):
    m = input("候補者の名前を入力；")
    list.append(m)


C = collections.Counter(list)
print(C.most_common()[0][0])