# 在/p 临近/v １９９７年/t 时/Ng
import random


def tocrfformat(data):
    crfFormat = []
    for line in data:
        words = line.split()[1:]
        for word in words:
            if "/tp" not in word:
                word = word.split('/')[0]
                length = len(word)
                if length == 1:
                    crfFormat.append(word[0] + "\t" + "S" + "\t" + "O")
                elif length == 2:
                    crfFormat.append(word[0] + "\t" + "B" + "\t" + "O")
                    crfFormat.append(word[1] + "\t" + "E" + "\t" + "O")
                else:  # length >= 3
                    crfFormat.append(word[0] + "\t" + "B" + "\t" + "O")
                    for i in range(1, length - 1):
                        crfFormat.append(word[i] + "\t" + "M" + "\t" + "O")
                    crfFormat.append(word[length - 1] + "\t" + "E" + "\t" + "O")

            else:  # 是时间词
                word = word.split('/')[0]
                length = len(word)
                if length == 1:
                    crfFormat.append(word[0] + "\t" + "S" + "\t" + "TS")
                elif length == 2:
                    crfFormat.append(word[0] + "\t" + "B" + "\t" + "TB")
                    crfFormat.append(word[1] + "\t" + "E" + "\t" + "TE")
                else:  # length >= 3
                    crfFormat.append(word[0] + "\t" + "B" + "\t" + "TB")
                    for i in range(1, length - 1):
                        crfFormat.append(word[i] + "\t" + "M" + "\t" + "TM")
                    crfFormat.append(word[length - 1] + "\t" + "E" + "\t" + "TE")
        crfFormat.append("\n")
    return crfFormat


f1 = open("199801.txt", encoding='gbk')
data = []
for line in f1.readlines():
    if line.strip():
        data.append(line)

f1.close()

f1 = open("prefix.txt", 'r', encoding='gbk')
prefix = set()
for word in f1.readlines():
    prefix.add(word.strip())
f1.close()

f2 = open("suffix.txt", 'r', encoding='gbk')
suffix = set()
for word in f2.readlines():
    suffix.add(word.strip())
f2.close()

newdata = []
time = []
for line in data:
    newline = ""

    words = line.split()
    words.append("。/w")
    i = 0
    while i < words.__len__() - 1:
        if words[i] not in prefix:
            newline += words[i] + " "
            i += 1
            continue
        else:
            length = 1
            while not words[i + length].endswith("/w") and words[i + length] not in suffix:
                length += 1
                continue
            if words[i + length] in suffix:
                timephrase = ""
                for count in range(length + 1):
                    timephrase += words[i + count].split("/")[0]
                time.append(timephrase)
                timephrase += "/tp"
                newline += timephrase + " "
                i += length + 1
                continue
            if words[i + length].endswith("/w"):
                for count in range(1, length + 1):
                    newline += words[i + count]
                i += length + 1
                continue
    newdata.append(newline)

f = open("事件型时间短语.txt", 'w')
for line in newdata:
    f.write(line + "\n")
f.close()

random.shuffle(newdata)
testSet = newdata[0:int(len(newdata) / 5)]
trainSet = newdata[int(len(newdata) / 5):]
crfTestSet = tocrfformat(testSet)
crfTrainSet = tocrfformat(trainSet)
f = open("CrfTestSet_EVENT.txt", 'w')
for a in crfTestSet:
    f.write(a + "\n")
f.close()
f = open("CrfTrainSet_EVENT.txt", 'w')
for a in crfTrainSet:
    f.write(a + "\n")
f.close()

f = open("timewords_Event.txt", 'w')
for word in time:
    f.write(word + "\n")
f.close()

print("end")
