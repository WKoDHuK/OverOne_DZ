import datetime


import random
Year = random.randint(1900,2022)
print(Year)

Year = datetime.datetime(year)


Year = int(input("Введите трехзначное число:"))
A = Year//100
B = (Year//10)%10
C = Year%10
print("сумма нашего трехзначного числа =")