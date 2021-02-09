import datetime

today_i = datetime.date.today()
today_s = str(today_i)

if today_s == "2020-01-28":
    print(today_i, " IS the day!")
else:
    print(today_i, " is NOt the day!")