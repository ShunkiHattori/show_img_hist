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
        