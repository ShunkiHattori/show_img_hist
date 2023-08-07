import datetime
import jpholiday

def ADtrans(year):
    today = datetime.date.today()
    eras = [
        {"year": 2018, "name": "令和"},
        {"year": 1988, "name": "平成"},
        {"year": 1925, "name": "昭和"},
        {"year": 1911, "name": "大正"},
        {"year": 1867, "name": "明治"},
    ]
    if year > today.year:
        return str(year) + "年の元号はまだわかりません"
    elif year < 1867:
        return "1867以上の数字を入力してください"
    else:
        for era in eras:

            baseYear = era["year"]
            era_name = era["name"]

            if year > baseYear:

                eraYear = year - baseYear

                if eraYear == 1:
                    return era_name + "元年"

                return era_name + str(eraYear) + "年"

        return "1867以上の数字を入力してください"


def week(year, month, day):
    dateValue = datetime.date(year, month, day)

    # 曜日(0～6)取得
    week = dateValue.weekday()

    if week == 0:
        print("月曜日")
    elif week == 1:
        print("火曜日")
    elif week == 2:
        print("水曜日")
    elif week == 3:
        print("木曜日")
    elif week == 4:
        print("金曜日")
    elif week == 5:
        print("土曜日")
    elif week == 6:
        print("日曜日")

    ans = jpholiday.is_holiday_name(datetime.date(year, month, day))
    if ans == None:
        print("祝日ではない")
    else:
        print(ans)
    print("現在時刻から入力した日まで"+str(abs(datetime.datetime.now() - datetime.datetime(year, month, day,0))))


def holiday(year, month):
    ans = jpholiday.month_holidays(year, month)
    print(ans)
        
        
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
    print(ADtrans(AD))

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
        week(AD, month, day)
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
    holiday(AD, month)
