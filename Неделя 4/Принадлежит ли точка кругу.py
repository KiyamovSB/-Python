def IsPointInCircle(x, y, xc, yc, r):
    h = ((x - xc)**2 + (y - yc)**2)**0.5
    if h > r:
        print('NO')
    else:
        print('YES')
    return

x, y, xc, yc, r = (float(input()) for i in range(5))
IsPointInCircle(x, y, xc, yc, r)
