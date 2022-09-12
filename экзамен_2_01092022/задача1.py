# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на:
# rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os.

import os
os.mkdir(r"C:\Users\alexd\Desktop\Folder_Exam") #создаем папку на рабочем столе
os.chdir(r"C:\Users\alexd\Desktop\Folder_Exam")  # заходим в эту папку
with open("test_1.txt" , "w") as file_1 :
    pass
with open("test_2.txt" , "w") as file_2 :
    pass
with open("test_3.txt" , "w") as file_3 :
    pass
os.rename(r"C:\Users\alexd\Desktop\Folder_Exam\test_1.txt" , "rename_1.txt")
os.rename(r"C:\Users\alexd\Desktop\Folder_Exam\test_2.txt" , "rename_2.txt")
os.rename(r"C:\Users\alexd\Desktop\Folder_Exam\test_3.txt" , "rename_3.txt")