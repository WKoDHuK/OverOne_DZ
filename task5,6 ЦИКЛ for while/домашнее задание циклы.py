# перемножить числа
# i = 1
# result = 1
# while i <= 100:
#     result += i
#     i += 1
# print(result)

#все числа кратные 5 в массив
# array=[]
# for i in range(1,500):
#     if i %5 == 0:
#         array.append(i)
# print(array)

#вывести все четные числа с 1 по 497
# for i in range(1,497):
#     if i %2 ==0:
#         print(i)


array_1 = [1,5,8,5,2,4,6,2,6,1,1,47,5,3,6,3,2,4,5,9,6]
array_2 = []
for i in array_1:
    if array_1.count(i) >=2:
        array_2.append(i)
print(array_2)

# Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив


