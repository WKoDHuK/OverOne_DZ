# Дана строка[“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.

mass = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
mass_2 = " "         #создаем массив с пробелом и ищем его в массиве, если находим, то бобавляем его в новый массив
mass_3 = []
for i in mass:
    if mass_2 in i:
        mass_3.append(i)
print(mass_3)
input("Нажмите Enter, чтобы выйти")

