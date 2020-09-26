p = int(input())
x = int(input())
y = int(input())
xy = float(x * 100 + y)
percentsxy = ((xy / 100 * p)+xy)
cop = int(percentsxy) % 100
rub = int(percentsxy) // 100
print(rub, cop, end=(' '))
