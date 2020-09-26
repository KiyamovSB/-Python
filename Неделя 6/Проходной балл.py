with open("input.txt", encoding="utf8") as file:
    k = int(file.readline().strip())
pupil = tuple()
pupilarray = [] * k
failed = []
file = open("input.txt", "r", encoding="utf8")
next(file)

for string in file:
    mypupil = (" ".join(map(str, string.split()[:-3])),
               int(string.split()[-3]), int(string.split()[-2]),
               int(string.split()[-1]))
    if mypupil[1] < 40 or mypupil[2] < 40 or mypupil[3] < 40:
        failed.append(mypupil)
    else:
        mypupil = (mypupil[0], mypupil[1], mypupil[2], mypupil[3],
                   int((mypupil[1] + mypupil[2] + mypupil[3])))
        pupilarray.append(mypupil)
pupilarray.sort(key=lambda p: p[4], reverse=True)
i = 0
for now in pupilarray:
    if k >= len(pupilarray) or k == 0:
        print("0")
        break
    elif now[4] > pupilarray[k][4]:
        i += 1
    elif [a[4] for a in pupilarray].count(max([a[4] for a in pupilarray])) > k:
        print("1")
        break
    else:
        print(pupilarray[i - 1][4])
        break
