import datetime as dt
import calendar

weekday = dt.date(1991,9,5).weekday()
print(calendar.day_name[weekday])

now = dt.datetime.today()

for i in range(100):
    print(now+dt.timedelta(days=i))
