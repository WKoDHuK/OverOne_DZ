A = int(input("Введите первое число:"))
B = int(input("Введите первое число:"))
C = int(input("Введите первое число:"))

# if A>B and A>C:
#     print("число a наибольшее")
# elif B>A and B>C:
#     print("число b наибольшее")
# elif C>A and C>B:
#     print("число c наибольшее")

    # еще вариант
if A > B and A>C:
        print("Наибольшее:", A)
else:
    if B>C:
        print("Наибольшее:", B)
    else:
        print("Наибольшее:", C)