#心配性な富豪

N = int(input("メニュー数を入力；"))
list1 = []
for i in range(N):
    m = int(input())
    list1.append(m)


list2 = list(set(list1))
list2.sort()
print(list2)
print(list2[-2])