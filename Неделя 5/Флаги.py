n = int(input())

print("+___ " * n)
print(*tuple(map(lambda i: "|{} /".format(i), range(1, n + 1))))
print("|__\ " * n)
print("|    " * n)
