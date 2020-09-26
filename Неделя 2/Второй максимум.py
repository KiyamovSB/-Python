N = int(input())
Max1 = N
Max2 = 0
while N != 0:
    N = int(input())
    if Max1 < N:
        Max2 = Max1
        Max1 = N
    elif N != 0 and Max2 < N:
        Max2 = N
print(Max2)
