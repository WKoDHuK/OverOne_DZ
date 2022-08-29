# Дан список [student1, student2, student3]
# с помощью цикла for добавить к каждому
# элементу списка слово “_good”. Вывести на экран.

spis = ["student1", "student2", "student3"]
spis_2 = []
for i in spis:
# в список каждому элементу добавим новый элемент
    i = i + "_good"
# и новыке элементы добавим в новый список
    spis_2.append(i)

    print(i)

print(spis_2)

input("Нажмите Enter, чтобы выйти")

