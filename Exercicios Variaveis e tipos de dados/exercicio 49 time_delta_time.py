"""
Time-Delta horas
"""
import datetime


t = datetime.time(9, 30, 45, 100000)#hora, minuto, segundo e microsegundo
print(t)
print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
#>>>2016-07-26 12:30:45.100000
print(dt.time())#pega só o horário
print(dt.year)#pega só ano

tdelta = datetime.timedelta(days = 7)
print(dt + tdelta)
#>>>2016-08-02 12:30:45.100000 (2016-07-26-->2016-08-02)

tdelta = datetime.timedelta(hours = 12)
print(dt + tdelta)# 12:30:45.100000 --> 00:30:45.100000
print('\t')
dt_today = datetime.datetime.today()
#>>>2019-08-28 12:34:03.502811
#retorns the current local time, with a timezone of none
dt_now = datetime.datetime.now()
#>>>2019-08-28 12:34:03.502811
#This give us the option to pass in a time zone
#If live the timezone empty then these are similar as .today()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

"""
for tz in pytz.all_timezones:
    print(tz)

pip install pytz
import pytz import timezone 

dt_utcnow = datetime.datetime.now(tz = pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
"""
