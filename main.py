import random


def tocrfformat(data):
    crfFormat = []
    for line in data:
        words = line.split()[1:]
        for word in words:
            if "/t" not in word:
                word = word.split('/')[0]
                length = len(word)
                if length == 1:
                    crfFormat.append(word[0] + " " + "S" + " " + "O" + "\n")
                elif length == 2:
                    crfFormat.append(word[0] + " " + "B" + " " + "O" + "\n")
                    crfFormat.append(word[1] + " " + "E" + " " + "O" + "\n")
                else:  # length >= 3
                    crfFormat.append(word[0] + " " + "B" + " " + "O" + "\n")
                    for i in range(1, length - 1):
                        crfFormat.append(word[i] + " " + "M" + " " + "O" + "\n")
                    crfFormat.append(word[length - 1] + " " + "E" + " " + "O" + "\n")

            else:  # 是时间词
                word = word.split('/')[0]
                length = len(word)
                if length == 1:
                    crfFormat.append(word[0] + " " + "S" + " " + "TS" + "\n")
                elif length == 2:
                    crfFormat.append(word[0] + " " + "B" + " " + "TB" + "\n")
                    crfFormat.append(word[1] + " " + "E" + " " + "TE" + "\n")
                else:  # length >= 3
                    crfFormat.append(word[0] + " " + "B" + " " + "TB" + "\n")
                    for i in range(1, length - 1):
                        crfFormat.append(word[i] + " " + "M" + " " + "TM" + "\n")
                    crfFormat.append(word[length - 1] + " " + "E" + " " + "TE" + "\n")

        crfFormat.append("\n")
    return crfFormat


f1 = open("199801.txt", encoding='utf-8')
data = []
for line in f1.readlines():
    if line.strip():
        data.append(line)

f1.close()
timewords = set()
# for line in data:
#     words = line.split()
#     timeword = ""
#     for word in words:
#         if "/t" in word:
#             timeword += word
#         elif timeword != "":
#             timeword = timeword.replace("/t", "")
#             timewords.add(timeword)
#             timeword = ""
newdata = []  # /t词合并后

for line in data:
    newline = ""
    words = line.split()
    words.append(" ")
    timeword = ""
    for i in range(words.__len__() - 1):
        if "/t" not in words[i] and timeword == "":
            newline += words[i] + " "
        elif "/t" in words[i]:
            timeword += words[i]
        else:
            timeword = timeword.replace("/t", "") + "/t"
            newline += timeword + " " + words[i] + " "
            timeword = ""
    newdata.append(newline)

f1 = open("prefix.txt", 'r', encoding='utf-8')
prefix = set()
for word in f1.readlines():
    prefix.add(word.strip())
f1.close()
newdata2 = []
for line in newdata:  # 前缀为prefix中词的时间词
    newline = ""
    words = line.split()
    words.append(" ")
    timeword = ""
    i = 0
    while i <= (words.__len__() - 1):
        if "/p" not in words[i]:
            newline += words[i] + " "
            i += 1
            continue
        else:
            if "/t" not in words[i + 1]:
                newline += words[i] + " "
                i += 1
                continue
            else:
                if words[i] not in prefix:  # 判断前缀是否在prefix表中
                    newline += words[i] + " "
                    i += 1
                    continue
                else:
                    timeword = words[i].replace("/p", "") + words[i + 1]
                    timewords.add(timeword)
                    newline += timeword + " "
                    i += 2

    newdata2.append(newline)

f2 = open("suffix.txt", 'r', encoding='utf-8')
suffix = set()
for word in f2.readlines():
    suffix.add(word.strip())
f2.close()
newdata3 = []
for line in newdata2:  # 后缀为suffix中词的时间词
    newline = ""
    timeword = ""
    words = line.split()
    words.append(" ")
    i = 0
    while i <= (words.__len__() - 1):
        if "/t" not in words[i]:
            newline += words[i] + " "
            i += 1
            continue
        elif "/t" in words[i] and "/f" not in words[i + 1]:
            newline += words[i] + " "
            timewords.add(words[i])
            i += 1
            continue
        else:
            if words[i + 1] not in suffix:  # 判断后缀是否在suffix中
                newline += words[i] + " "
                i += 1
                continue
            else:
                timeword = words[i].replace("/t", "") + words[i + 1].replace("/f", "/t")
                timewords.add(timeword)
                newline += timeword + " "
                i += 2
    newdata3.append(newline)

newdata4 = []
for line in newdata3:
    newline = ""
    words = line.split()
    words.append(" ")
    timeword = ""
    for i in range(words.__len__() - 1):
        if "/t" not in words[i] and timeword == "":
            newline += words[i] + " "
        elif "/t" in words[i]:
            timeword += words[i]
        else:
            timeword = timeword.replace("/t", "") + "/t"
            newline += timeword + " " + words[i] + " "
            timeword = ""
    newdata4.append(newline)


f = open("newdata.txt", 'w', encoding='utf-8')
for line in newdata4:
    f.write(line + "\n")
f.close()

random.shuffle(newdata3)
testSet = newdata3[0:int(len(newdata3) / 5)]
trainSet = newdata3[int(len(newdata3) / 5):]
crfTestSet = tocrfformat(testSet)
crfTrainSet = tocrfformat(trainSet)
f = open("CrfTestSet.txt", 'w', encoding='utf-8')
for a in crfTestSet:
    f.write(a)
f.close()
f = open("CrfTrainSet.txt", 'w', encoding='utf-8')
for a in crfTrainSet:
    f.write(a)
f.close()

out = open("timewords.txt", 'w', encoding='utf-8')
for word in timewords:
    word = word.split("/")[0]
    out.write(word + '\n')
out.close()
print("end")
