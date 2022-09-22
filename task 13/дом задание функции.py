# Напишите рекурсивную функцию
# которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел,
# каждое в диапазоне от 1 до 100

# def factorial(n):
#     if n != 0:
#         return n * factorial(n-1)   #рекурcивная функция, которая вызывает сама себя
#     else:
#         return 1
# print(factorial(5))

import random
lst = [random.randint(1,100) for lst in range(10)]
def factorial(n):


print(lst)
