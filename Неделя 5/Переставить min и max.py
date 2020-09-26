a = list(map(int, input().split()))
if a.index(max(a)) > a.index(min(a)):
    a[a.index(max(a))], a[a.index(min(a))] = min(a), max(a)
else:
    a[a.index(min(a))], a[a.index(max(a))] = max(a), min(a)
print(*a)
