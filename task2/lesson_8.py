# модуль math это библиотека

import math

AB = input("Длина первого катета:")  # функция input() возвращает строку
AC = input("Длина второго катета:")
# строки переводятся в вещественные числа

AB = float(AB)
AC = float(AC)

#находим гипотенузу по теореме Пифагора
# суммаа квадратов катетов равна квадрату гипотенузы
# функция sqrt() из модуля math извлекает квадратный корень
# оператор возводит в квадрат

BC = math.sqrt(AB ** 2 * AC ** 2)

# площадь прям треугол равна половине площади соотвествующ прямоугольника
S = ( AB * AC ) / 2
 # периметр находистя как сумма всех сторон

P = AB+AC+BC

print("Периметр=",P,"см")
print("Площадь=",S)






