
#
# num_set = set(1,2,3,1,2,3)
# print(num_set)

# множество удаляет дубликаты и повторяющиеся элементы

# создание пустого множества, указываем или SET или DICT
# x = set()
# print(type(x))


# доступ к элементам множества
#
# months = set(["jan", "Feb", "Mar", "Apr"])
# for i in months:
#     print(i)


# посик элемента в списке, выведет или True или False
# months = set(["jan", "Feb", "Mar", "Apr"])
# print("Mar" in months)


# добавление элемента во множество
# list_1 = ["jan", "Feb", "Mar", "Apr"]
# months = set(list_1)
# months.add("Dec")
# print(months)


# удаление элемента
            # discard удаляет по наименованию, индекса во множестве нет

# num_set = {1,2,3,4,5,6}
# num_set.discard(3)
# print(num_set)
            # remove удалит и покажет ошибку, если нет такого элемента
# num_set = {1,2,3,4,5,6}
# num_set.remove(8)
# print(num_set)

            # pop удаляет рандомный элемент и в принт выводит чсило которое УДАЛИЛ
# num_set = {1,2,3,4,5,6}
# print(num_set.pop())
# print(num_set)

            # CLEAR все эелементы удалит
# num_set = {1,2,3,4,5,6}
# print(num_set.clear())

            # обьединение множеств, обьединит и уберет дубликаты

# x = {1,2,3}
# y = {4,3,6}
# z = {7,4,9}
# output = x.union(y,z)
# print(output)


            # оператор | палочка

# x = {1,2,3}
# y = {4,3,6}
# z = {7,4,9}
# print(x|y|z)


            # пересечение множесвт & выводит дубликаты на экран
# x = {1,2,3}
# y = {4,3,6}
# print(x&y)

            # метод INTERSECTION

            # разниа (вычитание) множеств
            # удаляет из дубликаты из одной переменной
# a = {1,2,3}
# b = {4,3,6}
# print(a-b)
# print(b-a)

                # COPY метод
# months = {"jan", "Feb", "Mar", "Apr"}
# x = months.copy()
# print(x)

                # LEN
# months = {"jan", "Feb", "Mar", "Apr"}
# print(len(months))

                # FROZENSET  не изменяет множество

# my_set = frozenset([1,2,3,-10,40])
# print(type(my_set))

                # ИСКЛЮЧЕНИЯ дают обойти ошибку

# try:
#     k = 1/0
# except ZeroDivisionError:
#     k=0
# print(k)

               #
