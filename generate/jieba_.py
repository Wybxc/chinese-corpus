import jieba.posseg as pseg

while True:
    print(list(pseg.cut(input(''))))