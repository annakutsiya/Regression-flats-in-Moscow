from datetime import datetime, timedelta
today = datetime.today()
delta = timedelta (days =1)
yesterday = today - delta
delta_2 = timedelta (days =30)
days_ago_30 = today - delta_2
str = '01/01/25 12:10:03.234567'.replace(' ', '.').replace('01','1').replace('03', '3').replace('25', '2025')
import re
lst = re.split(r'[/:.]', str)
lst_2 =[]
for i in lst:
    lst_2.append(int(i))
lst_2[2], lst_2[0]=lst_2[0], lst_2[2]

# date_str = ', '.join(str(x) for x in lst_2)
# print (date_str)
new_type_date = datetime(*lst_2)
print(today)
print(yesterday)
print(days_ago_30)
print(new_type_date)
