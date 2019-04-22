def tocrfformat(data):
    crfFormat = []
    for line in data:
        words = line.split()[1:]
        for word in words:
            if "/t" not in word:
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
    return crfFormat