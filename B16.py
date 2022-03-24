#A±B Problem

a,b,c = map(int,input().split())

if b == 0:
    print("?")

elif a + b == c:
    print("+")

elif a - b == c:
    print("-")

else:
    print("!")


