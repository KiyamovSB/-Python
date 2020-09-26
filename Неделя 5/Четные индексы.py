a = list(map(int, input().split()))

k = 1

for i in a:
    if k % 2 == 1:
        print(i, end=' ')
    k += 1
