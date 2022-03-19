#長方形
"""
ある長方形の3つの辺の長さが与えられる。
残り1つの辺の長さを求めなさい。
"""

a,b,c = map(int,input().split())
d = 0
if a == b:
    d = d+c
elif a == c:
    d = d+b
else:
    d = d+a

print(d)