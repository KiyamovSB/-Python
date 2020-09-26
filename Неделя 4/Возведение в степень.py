def zxc(a, n):
    if n > 1:
        a = a * zxc(a, n - 1)
    else:
        a = a ** n
    return a

a, n = float(input()), float(input())
print(zxc(a, n))
