# создать словать и вывести возраст в принт
# dict_2 = {'name':'Alex', 'age':'36', 'city':'Dn'}
# print(dict_2['age'])

######################################################

#bmw = [x1, x3, x5]
#tesla = [model_X, mode_S, model_L]

# dict_1 = {'bmw': ['x1','x3','x5'],
#           'tesla': ['model_X','model_S','model_L']}
# print(dict_1['bmw'][0],dict_1['bmw'][2])
# print(dict_1['tesla'][0],dict_1['tesla'][2])

# создаем списки марок и моделей
# затем выводим 1 и 3 модель из списка

##########################################################

# d1 = {"a": 100, "b": 800, "c": 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# сравнивает значения ключей в разных словарях, можно любые ключи
# print(d1["b"] == d2["b"])

###########################################################
# перемоножить все значения
d1 = {"a": 100, "b": 200, "c": 300}
b = 1
for i in d1:
    b = b*d1[i]
    print(b)














# длина словаря
# months = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
#           7:'Jul',8:'Aug',9:'Sep',10:'Okt',11:'Nov',12:'Dec',}
# count = len(months)
# print(count)
# # считает парами

######################################################

# del удаление элемента из словаря

# salary = {'Director':120000.0,
#           'Secretary':101150.00,
#           'Locksmith':188200.00}
# print(salary)
# del salary['Secretary']# просто пробел
# print(salary)

#######################################################

# ИСПОЛЬЗОВАНИЕ ВЛОЖЕННЫХ СЛОВАРЕЙ

# position = {'Manager': {'Director', 'Deputy director'},
#             'Teacher':{'Specialist', 'Methodist', 'Senio Lecturer'},
#             'Staff': {'Cleaner', 'Porter', 'Watchman'}}
# count1 = len(position)
# count2 = len(position['Manager'])
# count3 = len(position['Staff'])
#
# print(position, 'len:', count1, '\n',
# position['Manager'],'len:', count2, '\n',
# position['Staff'],'len:', count3, '\n')


############################################################

# функция ZIP
# создание словаря из списков ключей и значений
# numbers = dict(zip([1,2,3], ['One', 'Two', 'Three']))
# print(numbers)

#############################################################
# обход словаря с помощью цикла for
# months = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
#            7:'Jul',8:'Aug',9:'Sep',10:'Okt',11:'Nov',12:'Dec',}
# for i in months:        # mn это как i
#     print(i, ':', months[i])    # : это для красоты

###############################################################

# сортировка словаря

# a = {'f':10, 'a':2, 'c':17}
# ak = a.keys()
# #print(ak)
# list_ak = list(ak)    # создаем из словаря ключей спиоск ключей
# #print(list_ak)
# list_ak.sort()       # сортируем список ключей
# #print(list_ak)
# b = {}      # создаем новый словарь пустой
# for i in list_ak:
#     print('(', i, ':', a[i], ')')   # скобочки тут для красоты
#     b[i]=a[i]      # к словарю b присваиваем значения a
# print(b)

