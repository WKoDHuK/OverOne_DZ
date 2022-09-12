a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
try:
    c = a/b
except ZeroDivisionError:
    c=0
    print(int(input('Введите заново число')))

print(c)
#
# try:
#    num_3 = num_1/num_2       # делим чсило на 0
# except ZeroDivisionError:    # видит ошибку деления на ноль
#     num_3=0                  # ставим что результат равен 0
#     print("Что то пошло не так")
# else:                        # если нормально все, то возведет в квадрат
#     print(num_3**2)
# finally:
#     print("Задача выполнена")