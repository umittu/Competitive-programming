#テスト評価
"""
テストの点数を入力するとその評価をするプログラムを作成せよ。
プログラムの仕様は以下の通り
・テストの点数として0以上100以下の整数を受け取る。
・テストの点数が59以下ならばBadを出力。
・60点以上89点以下ならばGoodと出力。
・90点以上99点以下ならばGreatと出力。
・100点ならばPerfectと出力。
"""
N = int(input("テストの点数を入力してください："))

if N<=59:
    print("Bad")
elif 60<=N<=89:
    print("Good")
elif 90<=N<=99:
    print("Great")
else:
    print("Perfect")
    






