# def factorial(n):
#     if n != 0:
#         return n * factorial(n-1)   #рекурcивная функция, которая вызывает сама себя
#     else:
#         return 1
# print(factorial(5))

###############################################################################################################
#
# def func(x): return x
# a1 = func
# a2 = a1
# print(a2(7))
############################################################

#АНОНИМНАЯ функция LAMDBA, упрощает,быстрее

# product = lambda x,y: x*y
# print(product(2,3))
# print(type(product))  #показывает какой тип
#########################################################################

# ФУНКЦИЯ ВНУТРИ ФУНКЦИИ

# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
# print(mul(3)(2))  # 3 относится к функции mul, 2 к функции helper

##############################################################################

# декоратор функции
# def first_test():
#     print('Test function 1')
#
# def second_test():
#     print('Test function 2')

def simple_decore(fn):
    print('Start function')
    fn()
    print('Stop function')

@simple_decore       #@ декорирует нашу функцию
def first_test():
    print('Test finction 1')

@simple_decore
def second_test():
    print('Test finction 2')
