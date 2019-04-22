f = open("CrfTrainSet.txt", 'r', encoding="utf-8")
i = 0
for line in f.readlines():
    i += 1
    list = line.split()
    if len(list) != 2 and len(list) != 0:
        print(i)
