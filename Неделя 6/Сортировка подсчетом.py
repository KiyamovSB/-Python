def CountSort(list_i):
    list_ii = [0] * (max(list_i) + 1)
    for now in list_i:
        list_ii[now] += 1
    b = 0
    for i in range(max(list_i) + 1):
        for j in range(list_ii[i]):
            list_i[b] = i
            b += 1
    return list_i


myList = list(map(int, input().split()))
print(*CountSort(myList))
