a = int(input())
if a % 10 >= 5 and a % 10 <= 9:
    print(a, "korov")
elif a % 10 == 1 and a != 11:
    print(a, "korova")
elif a >= 10 and a <= 20 or a % 10 == 0:
    print(a, "korov")
elif a % 10 >= 2 and a % 10 <= 4:
    print(a, "korovy")
