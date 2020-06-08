#标点及分词处理
def seg_sentence(sentence):
    sentence = sentence.strip()  # 去前后的空格
    sentence = sentence.replace('\n', '')  # 用后一字符''替换换行符
    sentence = re.sub('[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+', '', sentence)  # 去标点符号
    seg_list = jieba.cut(sentence, cut_all=False)  # 结巴分词
    # print("/".join(seg_list))#为数组seg_list设置分隔符/
    outstr = ''
    for word in seg_list:
        outstr += word
    return outstr