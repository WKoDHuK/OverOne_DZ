# Есть словарь песен группы Depeche Mode
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут.
# Создайте новый словарь тех песен, в название которых состоит из одного слова
import sys
dict_1 = { 'World in My Eyes': 4.76,
                       'Sweetest Perfection': 5.43,
                       'Personal Jesus': 4.56,
                       'Halo': 4.30,
                       'Waiting for the Night': 6.07,
                       'Enjoy the Silence': 4.6,
                       'Policy of Truth': 4.88,
                       'Blue Dress': 4.18,
                       'Clean': 5.68, }
print(sum(dict.values(dict_1)))
list_1 = []
for key in dict_1:
    if dict_1[key] > 5.0:
        list_1.append(key)
print(list_1)
dict_2 = {}
list_2 = []
for key1 in dict_1:
    if len(key1.split(' ')) == 1:
        dict_2[key1] = dict_1[key1]
print(dict_2)
