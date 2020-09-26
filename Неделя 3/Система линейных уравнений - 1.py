a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == 0:
    y = e / b
    x = (f - d * y) / c
    print(x, y)
elif b == 0:
    x = e / a
    y = (f - c * x) / d
    print(x, y)
elif c == 0:
    y = f / d
    x = (e - b * y) / a
    print(x, y)
elif d == 0:
    x = f / c
    y = (e - a * x) / b
    print(x, y)
elif a == 0 and d == 0:
    y = e / b
    x = f / c
    print(x, y)
elif b == 0 and c == 0:
    x = e / a
    y = f / d
    print(x, y)
else:
    y = (a * f - c * e) / (-1 * b * c + a * d)
    x = (e - b * y) / a
    print(x, y)
