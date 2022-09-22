# class car:
#     color = 'Grey'
#     def turn_on(self):
#         pass
#     def ride(self):
#         pass
# car_object = car()
# print(dir(car))

################################################################

# class car:
#     #статические поля (переменные класса), по умолчанию
#     default_color ="Grey"
#     default_weight = 5000
#
#     def __init__(self, color, model):
#         #динамические поля (переменные обьекта)
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         pass
# car_sport = car('red', 'model')

######################################################################
    # метод STR, переопредленеи методов в классе,
    # отвечает за ячейку памяти хранения, вызывает ячейку и ставит туда
# создание методов класса
#
# class car:
#     def __str__(self):
#         return "car class object"
#     def start(self):
#         print("Двигатель запущен")
# car_a = car()   # создан экземпляр car_a класса car
# print(car_a)
# car_b = car()
# print(car_b)

######################################################################

# методы ОБЫЧНЫЙ метод

# class Phone:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     def check_sim(self, mobile_operator):
#         if self.model == '1785' and mobile_operator == 'MTS'
#             print('Your mobile operator is MTS')





# статический метод справочного характера
#возвращает  хэш по номеру модели
# self внутри метода отсутсвтует
# class Phone:
#
#     @staticmethod
#     def model_hash(model):
#         if model == '1785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
# print(Phone.model_hash('1785'))
# # my_phone = Phone('red', '1785')
# # my_phone.check_sim('MTS')

#############################################################################

#уровни доступа к атрибутам

class H:
    def __init__(self):
        self.__money == 100
    def print_money(self):
        return self.__money
h = H()
h.__money

