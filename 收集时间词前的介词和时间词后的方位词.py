data = []
for i in range(199801, 199807):
    file = i.__str__() + ".txt"
    f = open("FullData/" + file, 'r', encoding='utf-8')
    data += f.readlines()
    f.close()

timewords = []
# for line in data:
#     words = line.split()
#     timeword = ""
#     for word in words:
#         if "/t" in word:
#             timeword += word
#         elif timeword != "":
#             timeword = timeword.replace("/t", "")
#             timewords.append(timeword)
#             timeword = ""
newdata = []  # /t词合并后
for line in data:
    newline = ""
    words = line.split()
    timeword = ""
    for word in words:
        if "/t" not in word and timeword == "":
            newline += word + " "
        if "/t" in word:
            timeword += word
        elif timeword != "":
            timeword = timeword.replace("/t", "") + "/t"
            newline += timeword + " "
            timeword = ""
    newdata.append(newline)

pwords = set()
for line in newdata:  # 前缀为介词的时间词
    words = line.split()
    timeword = ""
    for i in range(words.__len__() - 1):
        if "/p" not in words[i]:
            continue
        else:
            if "/t" not in words[i + 1]:
                continue
            else:
                timewords.append(words[i] + words[i + 1])
                pwords.add(words[i])
f = open("pwords.txt", 'w', encoding='utf-8')
for w in pwords:
    f.write(w + '\n')
f.close()

fwords = set()
for line in newdata:  # 前缀为后缀的时间词
    words = line.split()
    for i in range(words.__len__() - 1):
        if "/t" not in words[i]:
            continue
        elif "/t" in words[i] and "/f" not in words[i + 1]:
            timewords.append(words[i])
        else:
            timewords.append(words[i] + words[i + 1])
            fwords.add(words[i + 1])
f = open("fwords.txt", 'w', encoding='utf-8')
for w in fwords:
    f.write(w + '\n')
f.close()

out = open("timewords.txt", 'w', encoding='utf-8')
for word in timewords:
    out.write(word + '\n')
out.close()
print("end")
