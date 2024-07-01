import datetime
now = datetime.datetime.now()
print(now)
day = now.strftime("%d.%m.%Y-%H:%M:%S")
day2 = now.strftime("%c")
day3 = now.strftime("%x")
day4 = now.strftime("%X")
print(day)
print(day2)
print(day3)
print(day4)


date = datetime.datetime.today()
print(date.strftime('%A^%a'))
print(date.strftime('%B^%b'))


r_day = '01.09.08 Birthday'
day = datetime.datetime.strptime(r_day, '%d.%m.%Y')
print(day)
print(type(day))

import datetime

date = input()
dar = datetime.datetime.strptime(date,'%d %B %Y %H:%M')
print(dar)

now = datetime.datetime.now()
hour = now.strftime('%H')
print(hour)

file = open('text.txt', 'a')
file.write("Hello world")
file.close()

with open('text.txt', 'r') as file:
    info = file.read()
    print(info)