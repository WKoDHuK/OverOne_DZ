print ("Ноль в качестве знака операции завершит работу программы")
х = float(input("x="))
y = float(input("y="))
while True:
    s = input("Знак (+-*/):")
    if s == "0":
        break
    elif s == "+":
        print(x+y)
    elif s == "-":
        print(x-y)
    elif s == "*":
        print(x*y)
    elif s == "/":
        if y != 0:
            print(x/y)
        else:
            print("Деление на ноль")




