import random


def tocrfformat(data):
    crfFormat = []
    for line in data:
        words = line.split()[1:]
        if len(words) == 0:
            continue
        for word in words:
            if "/t" not in word:
                word = word.split('/')[0]
                length = len(word)
                for i in range(0, length):
                    crfFormat.append(word[i] + " " + "O" + "\n")


            else:  # 是时间词
                word = word.split('/')[0]
                length = len(word)


                if length >= 2:  # length >= 3
                    crfFormat.append(word[0] + " " + "B-PER" + "\n")
                    for i in range(1, length):
                        crfFormat.append(word[i] + " " + "I-PER" + "\n")


        crfFormat.append("\n")
    return crfFormat


def readFile(filename, data):
    f1 = open(filename, encoding='utf-8')
    for line in f1.readlines():
        if "/t" not in line:
            continue
        if line.strip():
            data.append(line)
    f1.close()


data = []
f = 199800
for i in range(6):
    f = f + 1
    readFile("FullData/" + f.__str__() + ".txt", data)



timewords = set()


f1 = open("prefix.txt", 'r', encoding='utf-8')
prefix = set()
for word in f1.readlines():
    prefix.add(word.strip())
f1.close()
newdata2 = []
for line in data:  # 前缀为prefix中词的时间词
    newline = ""
    words = line.split()
    words.append(" ")
    timeword = ""
    i = 0
    while i < (words.__len__() - 1):
        pre = words[i].split("/")[0]
        if pre not in prefix:  # 前词不在prefix表中
            newline += words[i] + " "
            i += 1
            continue
        else:  # 前词在prefix表中
            if "/t" not in words[i + 1]:  # 后词不是/t词
                newline += words[i] + " "
                i += 1
                continue
            else:  # 后词是/t词
                timeword = pre + words[i + 1]
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
    while i < (words.__len__() - 1):
        suf = words[i + 1].split("/")[0]
        if "/t" not in words[i]:  # 该词不是/t词
            newline += words[i] + " "
            i += 1
            continue
        elif "/t" in words[i] and suf not in suffix:  # 该词是/t词 但后词不是suffix词表中的词
            newline += words[i] + " "
            # timewords.add(words[i])
            i += 1
            continue
        else:  # 该词是/t词 而且 后词是suffix词表中的词
            timeword = words[i].replace("/t", "") + suf + "/t"
            # timewords.add(timeword)
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

for line in newdata4:
    words = line.split()
    for word in words:
        if "/t" in word:
            timewords.add(word)

f = open("newdata.txt", 'w', encoding='utf-8')
for line in newdata4:
    f.write(line + "\n")
f.close()

random.shuffle(newdata4)
testSet = newdata4[0:int(len(newdata4) / 10)]
devSet = newdata4[int(len(newdata4)/10):int(len(newdata4) / 10)*2]
trainSet = newdata4[int(len(newdata4) / 10)*2:]
f = open("TestSet.txt", 'w', encoding='utf-8', newline='\n')
for a in testSet:
    f.write(a + '\n')
f.close()
crfTestSet = tocrfformat(testSet)
crfTrainSet = tocrfformat(trainSet)
crfDevSet = tocrfformat(devSet)
f = open("example.test", 'w', encoding='utf-8', newline='\n')
for a in crfTestSet:
    f.write(a)
f.close()
f = open("example.train", 'w', encoding='utf-8', newline='\n')
for a in crfTrainSet:
    f.write(a)
f.close()
f = open("example.dev", 'w', encoding='utf-8', newline='\n')
for a in crfDevSet:
    f.write(a)
f.close()

out = open("timewords.txt", 'w', encoding='utf-8', newline='\n')
for word in timewords:
    word = word.split("/")[0]
    out.write(word + '\n')
out.close()
print("end")