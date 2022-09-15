# def is_year_leap(a):
#     return a%4==0 and a % 100 !=0 or a % 400 ==0  #делится на 4 без остатка и делится на 100 и не равно 0, или делится на 400 и не равно 0
# print(is_year_leap(int(input('Введите год:'))))


#
# def is_year_leap(a):
#     a = int(input())
#     return a%4==0 and a % 100 !=0 or a % 400 ==0
# a = int(input('Введите год:'))



# посчитать квадрат
# import math
# def square(a):
#     Perimetr = a*4
#     Plowad = a*a
#     Diagonal = a*math.sqrt(2)
#     return Perimetr,Plowad,Diagonal
# print(square(int(input('Введите сторону квадрата:'))))


# def season(a):
#     if a == 12 or a == 1 or a == 2:
#         print('это зима')
#     elif a == 3 or a == 4 or a == 5:
#         print('это весна')
#     elif a == 6 or a == 7 or a == 8:
#         print('это лето')
#     else:
#         print('это осень')
# n = int(input('Введите номер месяца:'))
# season(n)

# Написать функцию is_prime,
# принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

import random
def is_prime(a):
    d = 2
    while a % d != 0:
        d += 1
    return d == a
a = int(input('введите число:'))
print(is_prime(a))

