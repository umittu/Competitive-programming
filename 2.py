#気象情報は、世界中にさまざまな形で流れています。その一つの地上実況気象通報式では、視程を次の規則に従って、VVという値（通報式）に変換して報じます。
#1.0.1km未満：VV値は00とする。
#2.0.1km 以上5km 以下：距離(km)を10 倍した値とする。1桁の場合は上位に0を付する。
#3.6km 以上30km以下：距離（km）に50を足した値とする。
#4.35km以上70km以下：距離（km）から30を引いて5で割った後、80を足した値とする。
#5.70kmより大きい：VVの値は89とする。
#いま、あなたに指定の距離をメートルで与えるので、上記のルールに従って計算されるVV値の値を出力しなさい。

A=int(input("視程を入力してください(m)："))
a=A/1000
if a<0.1:
    B=0
    print("VV値は",B,"mです。")
elif 0.1<=a<=5:
    B=a*10
    if B<10:
        b=str(B)
        C="0"+b
        print("VV値は",C,"mです。")
    else:
        print("VV値は",B,"mです。")
elif 6<=a<=3:
    B=a+50
    print("VV値は",B,"mです。")
elif 35<=a<=70:
    B=((a-30)/5)+80
    print("VV値は",B,"mです。")
else:
    B=89
    print("VV値は",B,"mです。")