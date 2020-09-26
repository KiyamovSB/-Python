a, b, c = int(input()), int(input()), int(input())
if a <= c <= b:
    (b, c) = (c, b)
elif b <= a <= c:
    (a, b) = (b, a)
elif c <= a <= b:
    (a, b, c) = (c, a, b)
elif b <= c <= a:
    (a, b, c) = (b, c, a)
elif c <= b <= a:
    (a, c) = (c, a)
print(a, b, c)
