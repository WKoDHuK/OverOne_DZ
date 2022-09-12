# Создайте словарь из строки
# ' An apple a day keeps the doctor away'
# следующим образом: в качестве ключей возьмите символы строки,
# а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку

a = 'An apple a day keeps the doctor away'
dic = {key:a.count(key) for key in a}
print(dic)