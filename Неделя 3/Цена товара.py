n = float(input())
rub = int(n // 1)
kop = int(round(n % 1, 2) * 100)
print(rub, kop, sep=' ')
