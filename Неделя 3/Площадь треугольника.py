import math
a, b, c = float(input()), float(input()), float(input())
p = float((a+b+c) / 2)
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)
