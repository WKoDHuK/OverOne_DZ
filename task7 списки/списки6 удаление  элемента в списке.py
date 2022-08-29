# elements = [1,3,"a",6,"b"]
# del elements[1]
# print(elements)


elements = [1,3,"a",6,"b"]
elements.remove("a")
del elements[1]
print(elements)


# del удаляет по индексу
# remove удаляет по первому вхождению, если например две буквы а, то удалит только первую попавшуюся
# pop удаляет и показывает удаленный элемент