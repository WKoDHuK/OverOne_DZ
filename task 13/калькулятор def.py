def calc():
    while(True):
        req = input(': ')
        if req == '':
            break
        print(req+'='+str(eval(req)))
calc()