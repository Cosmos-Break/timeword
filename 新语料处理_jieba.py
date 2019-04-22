import jieba
jieba.load_userdict("mydict.txt")
import jieba.posseg as pseg
# seg_list = jieba.cut("我来到北京清华大学")
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
# words = pseg.cut("我来到北京清华大学")
# print(type(words))
# print(words)
# for word, flag in words:
#     print(word + "/" + flag)


f = open("Newcorpus.txt", encoding='utf-8')
newdata = []
for line in f.readlines():
    newline = ""
    words = pseg.cut(line)
    for word, flag in words:
        newline += word + "/" + flag + " "
    newdata.append(newline)
f.close()

f = open("NewcorpusSEG.txt", 'w', encoding='utf-8')
for line in newdata:
    f.write(line + "\n")
f.close()

print("end")
