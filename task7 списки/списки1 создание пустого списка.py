# создание рандомного списка и выбор из этого списка элементов

import random
c = [random.randint(0,100) for i in range(10)] # 10 значит из списка взято 10 элементов
print(c)

print(c[0])
print(c[-1])
print(c[5])
print(c[-4])