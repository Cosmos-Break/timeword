# coding=utf-8
# True Positive （真正, TP）被模型预测为正的正样本；可以称作判断为真的正确率
# True Negative（真负 , TN）被模型预测为负的负样本 ；可以称作判断为假的正确率
# False Positive （假正, FP）被模型预测为正的负样本；可以称作误报率
# False Negative（假负 , FN）被模型预测为负的正样本；可以称作漏报率

# 准确率（正确率）=所有预测正确的样本 / 总的样本  （TP + TN） / 总
# 精确率 = 将正类预测为正类 / 所有预测为正类
# TP /（TP + FP）
# 召回率 = 将正类预测为正类 / 所有正真的正类
# TP /（TP + FN）
# F值 = 正确率 * 召回率 * 2 / (正确率 + 召回率) （F
# 值即为正确率和召回率的调和平均值）
TP = 0
FP = 0
FN = 0
TN = 0
f = open("result", 'r', encoding='utf-8')
FPlist = []
FNlist = []
for line in f.readlines():
    list = line.split()
    if len(list) < 1:
        continue
    if list[1] == list[2]:  # 预测对了
        if list[1] == 'O':  # 不是预测为不是 True negative
            TN += 1
        else:  # True positive
            TP += 1
    else:  # 预测错了
        if list[1] == 'O':  # 不是预测为是 False positive
            FP += 1
            FPlist.append(list[0])
            if list[2] == "TE":
                FPlist.append("\n")

        else:  # 是预测为不是 False negative
            FN += 1
            FNlist.append(list[0])
            if list[1] == "TE":
                FNlist.append("\n")

f.close()

print("TP = ", TP)
print("FN = ", FN)
print("FP = ", FP)
print("TN = ", TN)

if TN + TP + FP + FN == 0:
    print("error")
else:
    x = (TN + TP) / (TN + TP + FP + FN)  # 准确率
    P = TP / (TP + FP)  # 精确度
    R = TP / (TP + FN)  # 召回率
    F1 = 2 * P * R / (P + R)

f = open("FPlist.txt", 'w', encoding="utf-8")
f.writelines(FPlist)
f.close()

f = open("FNlist.txt", 'w', encoding="utf-8")
f.writelines(FNlist)
f.close()

print("准确度为：", x)
print("精确度为：", P)
print("召回率为：", R)
print("F1值为：", F1)
