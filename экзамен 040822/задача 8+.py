# Вам передан массив чисел.
# Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5

array = [1,5,2,9,2,9,1]
for i in array:                # если в моем массиве есть число встечающееся меньше 2х раз
    if array.count(i) < 2:
        print(i)

input("Нажмите Enter, чтобы выйти")