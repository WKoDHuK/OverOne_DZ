# print("Добро пожаловать в наше казино!")
# print("Вы у игрового стола игры Рулетка")
# print("Сделайте Вашу ставку, выберите число и цвет")
import random
num = random.randint(1,10)
color = random.randint(1,2)
c = ""
if color == 1:
    c = "красный"
else:
    color = "черный"
shanse = 5
choice_number = int(input("Выберите номер:"))
choice_color = input("Выберите цвет:")
if choice_number and choice_color == c:
    print('победил')
elif choice_number and choice_color != c:
    print('победил, но без цвета')
    print('осталось',shanse, 'попыток')
choice_number = int(input("Выберите номер:"))
choice_color = input("Выберите цвет:")
if choice_number and choice_color == c:
    print('победил')
elif choice_number and choice_color != c:
    print('победил, но без цвета')
    print('осталось',shanse-1, 'попыток')
choice_number = int(input("Выберите номер:"))
choice_color = input("Выберите цвет:")
if choice_number and choice_color == c:
    print('победил')
elif choice_number and choice_color != c:
    print('победил, но без цвета')
    print('осталось',shanse-2, 'попыток')
choice_number = int(input("Выберите номер:"))
choice_color = input("Выберите цвет:")
if choice_number and choice_color == c:
    print('победил')
elif choice_number and choice_color != c:
    print('победил, но без цвета')
    print('осталось',shanse-3, 'попыток')
choice_number = int(input("Выберите номер:"))
choice_color = input("Выберите цвет:")
if choice_number and choice_color == c:
    print('победил')
elif choice_number and choice_color != c:
    print('победил, но без цвета')
    print('осталось',shanse-4, 'попыток')
shanse +=1
print('Вы использовали пять попыток угадать число и цвет фишки')




