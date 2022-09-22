# class Example:
#     a = 2      # в статических полях они же являются ГЛОБАЛЬНЫМИ
#     b = 3
#     def __init__(self, t, r):
#         self.t=t
#         self.r=r
#     def func(self):
#         self.c=5
#         print(self.c)
#     def func1(self):
#         return self.a + self.b
#     def func2(self):
#         return self.t**self.r   #возводим одну переменную в другую
# Example_obj = Example(5,7)
# print(Example_obj.a)      #вывести переменную а
# print(Example_obj.func1())
# print(Example_obj.func2())
# Example_obj.func()   # если print внутри, то снаружи он не нужен

########################################################################################

# class calc:
#
#     def __init__(self):
#         self.func4()
#
#     def func(self):
#         return self.a + self.b
#
#     def func1(self):
#         return self.a - self.b
#
#     def func2(self):
#         return self.a * self.b
#
#     def func3(self):
#         if self.b == 0:
#             return 'error'
#         else:
#             return self.a / self.b
#
#     def func4(self):
#         self.a = int(input(''))
#         self.b = int(input(''))
# while True:
#     print("+,-,*,/")
#     x = input('ВВедите операцию:')
#     print("Numbers:")
#     Thecalc = calc()
#     if x == "6":
#         break
#     if x == "+":
#         print(calc.func())
#     if x == "-":
#         print(calc.func1())
#     if x == "*":
#         print(calc.func2())
#     if x == "/":
#         print(calc.func3())

#######################################################################

class Human:
    #статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # динамические поля
        # публичные
        self.name = name
        self.age = age
        # приватные
        self.__money = 1000
        self.__house = 'Дом'
    # справочный метод
    def info(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Money:{self.__money}')
        print(f'House:{self.__house}')
    # статический справочный метод
    @staticmethod
    def default_info():
        print(f'Default Name:{Human.default_name}')
        print(f'Default Age:{Human.default_age}')
    def earn_money(self, amount):
        self.__money += amount
        # прибаленна сумма денег. и итоговое значение составляет:
        print(f'Earned:{amount} money! Current value: {self.__money}')
# вызов статического метода, не требует создание экземпляра
Human.default_info()
# создание обьекта Human
Alexander = Human('Sasha', 18)
Alexander.info()

Alexander.earn_money(5000)
Alexander.earn_money(20000)
Alexander.info()

###############################################################################




