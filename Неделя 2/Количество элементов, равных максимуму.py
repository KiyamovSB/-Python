now = -1
maxNum1 = 0
maxNum2 = 0
while now != 0:
    now = int(input())
    if now > maxNum1:
        maxNum1, maxNum2 = now, 1
    elif now == maxNum1:
        maxNum2 += 1
print(maxNum2)
