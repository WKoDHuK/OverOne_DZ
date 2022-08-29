start = int(input("\nВведите начальный индекс среза:"))
finish = int(input('Введите конечный индекс среза:'))
print("Срез inventory [", start, ":", finish,") - это", end="")
print(inventory[start:finish])
