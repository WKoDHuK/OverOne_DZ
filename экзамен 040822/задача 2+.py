# Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений

import math    #импорт математического модуля

a = 7
b = 9
c = 11

y = 0.25 * int(math.sin(a+b-c) + math.sin(b+c-a) + math.sin(c+a-b) - math.sin(a+b+c))

print(y)
input("Нажмите Enter, чтобы выйти")


# a = 7
# y = ((((1+a+a**2)/(2*a+a**2))+2-((1-a+a**2)/(2*a-a**2)))**-1*(5-2*a**2))
# print(y)



