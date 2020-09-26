a = list(map(int, input().split()))
k = -1
k2 = -1
max = 0
for i in a:
    k2 += 1
    if i >= max:
        max = i
        k += 1
        if k != k2:
            k = k2

print(max, k)
