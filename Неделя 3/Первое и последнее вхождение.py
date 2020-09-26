i = str(input())
if 'f' in i:
    print(i.find('f'))
    b = int(i.find('f'))
    b = b + 1
    c1 = i[b:]
    if 'f' in c1:
        print(i.rfind('f'))
