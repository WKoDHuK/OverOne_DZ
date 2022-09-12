# Ввести 10 чисел, данные числа добавить их во множество
from typing import Set, Any

import random
set_1 = set(random.randint(0,100) for i in range(10))
print(set_1)