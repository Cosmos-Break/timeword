# coding=utf-8
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

random.shuffle(data)
testSet = data[0:int(len(data) / 5)]
trainSet = data[int(len(data) / 5):]
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

print("end")
