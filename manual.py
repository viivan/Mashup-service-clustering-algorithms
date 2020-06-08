#输入：人工筛选功能名词
#输出：直接由Word2Vec转化的Mashup服务特征向量
def get_data(function_str):

    doc_vec=[]
    # 获取功能名词
    word_list = []
    for s in function_str:
        simple_list = str(s).split(",")
        word_list.append(simple_list)
    # 利用word2vec计算
    # 加载word2vec
    print("开始加载model")
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative.bin', binary=True)
    tf_idf_vec = []
    i = 0
    for vec in word_list:
        print(i)
        func_vec = np.zeros(300)
        for w in vec:
            try:
                wv = np.array(model[w])
                func_vec += wv
            except KeyError:
                continue
        doc_vec.append(func_vec)
        i += 1

    return doc_vec