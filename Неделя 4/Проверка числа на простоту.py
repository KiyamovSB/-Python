def IsPrime(n):
    i = 2
    prime = False
    while i <= n ** 0.5:
        if n % i == 0:
            return prime
        i += 1
    return not(prime)

n = int(input())
if n == 2 or IsPrime(n):
    print('YES')
else:
    print('NO')
