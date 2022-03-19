#掛け算の最大値
"""
正の偶数Aが与えられる。
x+y=Aとなる正の整数x,yのうち、x*yが最大となるものを選びその値を出力しなさい。
"""


A = int(input())

list=[]

for x in range(1,A):
    y = A-x
    z = x*y
    list.append(z)
    x = x-1

print(max(list))