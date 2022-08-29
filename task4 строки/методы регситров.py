s = 'hello everybody'
s_2 = 'Hello Everybody'
s_3 = 'Hello everybody'
#делаем строку заголовком
print(s.title())
# начинаем строку с заглавной буквы, остальнрые слова в строке ставит с маленькой
print(s.capitalize())
# переводим строку в верхний регистр
print(s.upper())
# переводим строку в нижний регситр
print(s.lower())
# инверсия регистра
print(s_2.swapcase())
#проверяем, являются ли строки заголовками, каждое слово в строке с Большой буквы
print(s.istitle())
print(s_2.istitle())
print(s_3.istitle())


