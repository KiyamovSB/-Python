import sys
input_data = sys.stdin.readlines()
candidaty = dict()
putin = list()
for l in input_data:
    candidaty[l] = candidaty.get(l, 0) + 1
for l in candidaty:
    putin.append((candidaty[l], l))
putin = sorted(putin)
if putin[-1][0] > len(input_data) / 2:
    print(putin[-1][1])
else:
    print(putin[-1][1], putin[-2][1], sep="")
