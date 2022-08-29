with open('www.txt') as f:
    s = f.readlines()
    print(s)
for i in s:
    i = i.replace('_', ' ')
    l = i.split(' ')
print(l)
sum(0)
for i in l:
    if i.isdigit():
        i = int(i)
        sum += i
print(sum)
