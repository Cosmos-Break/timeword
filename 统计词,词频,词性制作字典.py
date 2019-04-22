f = open("199801.txt")
dic = {}
# key = "1997年"
# val = [4, 't']
# dic[key] = val
# dic[key][0]+=1
print(dic)
for line in f.readlines():
    entry = line.split()[1:]
    for word in entry:
        wordAndFlag = word.split('/')
        key = wordAndFlag[0]
        if key not in dic:
            val = [1, wordAndFlag[1]]
            dic[key] = val
        else:
            dic[key][0] += 1

f.close()

f = open("dict.txt", 'w', encoding='utf-8')
for key, val in dic.items():
    f.write(key + " " + val[0].__str__() + " " + val[1] + "\n")
f.close()
print("end")
