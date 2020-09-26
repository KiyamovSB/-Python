def MinDivisor(n):
    i = 1
    sqrt = n**0.5
    while True:
        i += 1
        if i >= 50000:
            return n
        elif n % i == 0 and i > sqrt:
            return n
        elif n % i == 0 and i <= sqrt:
            return i

print(MinDivisor(int(input())))
