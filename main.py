import func

print("1.西暦を和暦に変換")
print("2.西暦、月、日からその日の曜日と祝日かどうかを出力")
print("3.西暦、月からその月の祝日を検索")
sel = 0
print("")
while True:
    try:
        sel = int(input("使う機能の番号を入力してください(半角):"))
    except ValueError:
        print("半角数字で入力してください")
    if sel != 1 and sel != 2 and sel != 3:
        print("1,2,3から選んでください")
    if sel == 1 or sel == 2 or sel == 3:
        break


if sel == 1:
    print("")
    print("西暦を和暦に変換します")
    AD = int(input("西暦を入力してください(半角で1867以上2023以下の数字):"))
    print(func.ADtrans(AD))

if sel == 2:
    print("")
    print("西暦、月、日からその日の曜日と祝日かどうかを出力します")
    while True:
        try:
            AD = int(input("西暦を入力してください(半角):"))
        except ValueError:
            print("半角数字で入力してください")
        else:
            break

    while True:
        try:
            month = int(input("月を入力してください(半角):"))
        except ValueError:
            print("半角数字で入力してください")
        else:
            if month > 12 or month < 1:
                print("1～12から選んでください")
            else:
                break

    while True:
        try:
            day = int(input("日を入力してください(半角):"))
        except ValueError:
            print("半角数字で入力してください")
        else:
            if day > 31 or day < 1:
                print("1～31から選んでください")
            else:
                break
    try:
        func.week(AD, month, day)
    except ValueError:
        print("その日付は存在しません")

if sel == 3:
    print("")
    print("西暦、月からその月の祝日を検索します")
    while True:
        try:
            AD = int(input("西暦を入力してください(半角):"))
        except ValueError:
            print("半角数字で入力してください")
        else:
            break

    while True:
        try:
            month = int(input("月を入力してください(半角):"))
        except ValueError:
            print("半角数字で入力してください")
        else:
            if month > 12 or month < 1:
                print("1～12から選んでください")
            else:
                break
    func.holiday(AD, month)
