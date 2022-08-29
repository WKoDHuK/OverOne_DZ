# создал случйный список из 10 чисел и указал мин и макс
# преобразовал из списка в кортеж затем
# import random
# list = [random.randint(0,100) for i in range(10)]
# tuple_1 = tuple(list)
# print(list)
# print("max", max(tuple_1), "min", min(tuple_1))

# создал 2 новых списка и преобразовал их в кортежи
# узнал сколько 0 в кортеже
import random
# list = [random.randint(0,5) for i in range(5)]
# list_2 = [random.randint(-5,0) for i in range(5)]
# tuple_1 = tuple(list)
# tuple_2 = tuple(list_2)
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3, '\n Количесвто нулей:', tuple_3.count(0))
# \n переносит на новую строку



# преобразовал без скобок
# tuple_1 = ("Сегодня", "8","число", "август")
# tuple_2 = (','.join(tuple_1))
# print(tuple_2)


# посчитать сумму кортежей и вывести на экран какой больше
# a = (13,5,43,49,67,32,12,98,6,10,34,20,55,68,14,60,14)
# b = (53,21,4,23,76,3,43,12,54,342,21)
# sum(a)
# sum(b)
# if a>b:
#     print("Сумма больше в кортеже-",sum(a))
# else:
#     print("Сумма больше в кортеже-",sum(b))
# print("min в кортеже а", min(a), "\n min в кортеже b", min(b))
# print(a.index(min(a)))
# print(b.index(min(b)))




# 1 Создайте  кортеж с цифрами от 0 до 9 и посчитайте сумму
# tuple_1 = (0,1,2,3,4,5,6,7,8,9)
# sum(tuple_1)
# print(sum(tuple_1))


# 2 Выведите статистику частности букв в кортеже
# long_word = ('t','f','d','t','f','d','t','f','d','t','f','d')
# print(long_word.count('t'))
# print(long_word.count('f'))
# print(long_word.count('d'))



# #3 Допишите скрипт для расчета средней температуры
# # Постарайтесь посчитать количество дней на основе week_temp.
# # Так наш скрипт сможет работать c данными за любой период
#
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days = 7
# mean_temp = sum_temp / days
# print(int(mean_temp))




# Задание №1
# Найти самое длинное слово в строке.

# list_1 = ["Найти самое длинное слово в строке"]
# list_2 = ('Найти самое длинное слово в строке'.split(' '))
# list_3 = []
# for i in list_2:
#     list_3.append(len(i))
# ind = list_3.index(max(list_3))   # определяет индекс самого длинного слова в строке
# print("Самое длинное слово в строке:", list_2[ind])
# print(ind)




# Задание №2
# Преобразовать текст в список слов с удалением знаков препинания.
list_1 = ['Сегодня, 10 августа, был удачный день - день возможности отдохнуть!']
