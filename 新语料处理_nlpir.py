import pynlpir  # 引入依赖包
pynlpir.open()  # 打开分词器
s = 'NLPIR分词系统前身为2000年发布的ICTCLAS词法分析系统，从2009年开始，' \
    '为了和以前工作进行大的区隔，并推广NLPIR自然语言处理与信息检索共享平台，' \
    '调整命名为NLPIR分词系统。'  # 实验文本

s2 = '迈向充满希望的新世纪——一九九八年新年讲话（附图片１张）,你是我的菜'
li = pynlpir.segment(s2)  # 默认打开分词和词性标注功能
# 样本输出: [('NLPIR', 'noun'), ('分词', 'verb'), ('系统', 'noun'), ('前身', 'noun'), ('为', 'preposition'), ('2000年', 'time word'), ('发布', 'verb'), . . . ]
pynlpir.close()
print(li)
print("end")