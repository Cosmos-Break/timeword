fw = open("teeeeee.txt", 'w', encoding='utf-8', newline='\n')
i = 1
with open("CrfTestSet.txt", 'r', encoding='utf-8') as f:
    list = f.readlines()
    for line in list:
        # print(line.strip())
        re = line.strip()
        fw.write(re)
        if re == "":
            fw.write('\n')
            print(i)
        i += 1

fw.close()
