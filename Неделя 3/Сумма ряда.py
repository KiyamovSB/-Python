i = float(input())
n, r = 1, 0
while n != i + 1:
    r += (1 / n**2)
    n += 1
print(r)
