#花占い
n = int(input())
list=[]
for i  in range(n):
    m = int(input())
    list.append(m)

x = 0
for j in range(n):
    if list[j] % 6 == 2:
        x = x+1
    elif list[j] % 6 == 4:
        x = x+1
    elif list[j] % 6 == 5:
        x = x+2
    elif list[j] % 6 == 0:
        x = x+3

print(x)
