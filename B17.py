#choku語

s = str(input())

if len(s) == 0:
    print("YES")

else:
    if s[-1] == 'h' and s[-2] == 'c':
        print("YES")
    elif s[-1] == 'o':
        print("YES")
    elif s[-1] == 'k':
        print("YES")
    elif s[-1] == 'u':
        print("YES")
    else:
        print("NO")