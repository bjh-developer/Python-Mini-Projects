#Calendar module tutorial by Clever Programmer (YT account name), Python 3

import calendar, datetime, time 

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 3))
print()

print(calendar.monthcalendar(2020, 3))
print()

print(calendar.calendar(2020))
print()

day_of_the_week = calendar.weekday(2020, 3, 29)
print(day_of_the_week)
print()

is_leap = calendar.isleap(2020)
print(is_leap)
print()

how_many_leap_days = calendar.leapdays(2000,2005)
print(how_many_leap_days)