#Напишите программу, демонстрирующую работу try\except\finally

a = [1,2,3,4,5]
numb = []
try:
    for i in a:
        numb.append(int(numb))
except ValueError:
    print('Кажется это не число')
except TypeError:
    print('Это тоже не число')
else:
    print('Это числа')
finally:
    print('Океюшки')