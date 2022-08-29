# def a_function():
#     print("You just created a function!")
# a_function()

# def empty_function():
#     pass

############################################################

# функция суммы чисел в списке до 10
# def summa():
#     sum = 0
#     for i in range(10):
#         sum += 1
#     print(sum)
# summa()

###################################################
# ПЕРЕДАЧА АРГУМЕНТОВ В ФУНКЦИИ

# def ad(a,b):
#     return a + b   # не выводит на экран, считает внутри компьютера
# print(ad(1,2))
#
# def ad(a,b):
#     print (a+b)   # если 2 принта то выведет только первый принт
# print(ad(1,2))

def ad(a,b):
     return a + b
print(ad(a=2, b=3))

total = ad (b=4, a=5)
print(total)

