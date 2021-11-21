import calendar
weekdays = list(map(lambda x:x.upper(),list(calendar.day_name)))
mm,dd,yy = list(map(int,input().split()))
print(weekdays[calendar.weekday(yy, mm, dd)])