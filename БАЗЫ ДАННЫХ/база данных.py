import sqlite3

#создаем БД
conn = sqlite3.connect('name1.db')

# создаем обьект cursor, который позволяет нам взаимодействовать с БД и добавлять записи
cursor = conn.cursor()

# #создадим таблицу с двумя текстовыми колонками
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
#
# # заполняем таблицу
# cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES('hello', 'world')''')
#
# # сохраняем изменения
# conn.commit()
# #
cursor.execute('''SELECT*FROM tab_1''')
#print(cursor.fetchall())    # fetchall метод вывода таблицы
#
# d = "red"
# f = "black"
#
# cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''', (d,f))
# conn.commit()
#
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)

#уддаление записи из таблицы по id , по значению
# cursor.execute('''DELETE FROM tab_1 WHERE id = 2''')
# conn.commit()
#
# cursor.execute('''DELETE FROM tab_1 WHERE col_1 = 'red' ''')
# conn.commit()
#
# cursor.execute('''DELETE*FROM tab_1''')
# conn.commit()

#обновление данных в таблице
t = 8  # id с номером 8
cursor.execute('''UPDATE tab_1 SET col_1='world' WHERE id=?''', (t,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k=cursor.fetchall()
print(k)
