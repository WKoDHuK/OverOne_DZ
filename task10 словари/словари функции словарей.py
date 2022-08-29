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
#
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
numbers = dict(zip([1,2,3], ['One', 'Two', 'Three']))
print(numbers)

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
#
