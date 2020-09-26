X = float(input())
Y = float(input())
day = 1
while X < Y:
    X = X + X/100*10
    day = day + 1
print(day)
