# домашнее задание на определение,является ли год високосным
import random
YEAR = random.randint(1000,2022)
print(YEAR)

HightYear = YEAR
if YEAR % 4 ==0 and year % 100 != 0 :
    print("год високосный")
elif YEAR % 400 == 0 :
    print("Год является високосным")
else:
    print("Год не является високосным")
