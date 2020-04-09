"""
Time-Delta Dias
"""

import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days = 7)

print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2020, 3, 13)
till_bday = bday - tday
print(till_bday)
#>>>198 days, 0:00:00
#para sair só os dias 
print(till_bday.days)
print(till_bday.total_seconds())
