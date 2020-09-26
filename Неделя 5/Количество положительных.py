a = input().split()
j = 0
for i in range(0, len(a)):
    if int(a[i]) > 0:
        j = j + 1
print(j)
