#构造MFSF向量
#输出：所有MFSF向量
def MFSF():
    doc_vec=[]
    name_str = []
    line_str = []
    tag_str = []
    wordnet_lemmatizer = WordNetLemmatizer()
    df = pd.read_excel("exp.xlsx", usecols=[0, 1, 5])  # df为DataFrame（数据框）类型
    for index, row in df.iterrows():
        name_str.append(row['name'])
        line_str.append(row['description'])
        tag_str.append(row['tag'])

    # 词性标注
    word_list = []  # word_list存储描述分词后的单词，供tfidf训练使用
    noun_list = []  # 用于存放每条描述的名词
    stopwords = stopwordslist('./stop/stop_words_eng.txt')  # 这里加载停用词表
    stopwords2 = stopwordslist('./stop/stop_words_eng2.txt')  # 这里加载停用词表2

    noun_set_len = 0  # 记录所有服务描述的名词平均个数
    for (paragraph, name) in zip(line_str, name_str):
        # line_seg = seg_sentence(paragraph.lower())# 返回去除标点以及停用词后的字符串
        dict = {}  # 词性关系注入词典dict
        noun_set = set()
        word_temp = []
        word_temp2 = []
        paragraph = paragraph.strip()
        # paragraph = paragraph.lower()
        sens = nltk.sent_tokenize(paragraph)  # 按句子分割描述段落
        words = [nltk.word_tokenize(sentence) for sentence in sens]  # 分词
        pos_tags = [nltk.pos_tag(tokens) for tokens in words]  # 标注词性
        temp_index = 0
        for tag in pos_tags:
            for word, pos in tag:
                if word in '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' or not wordnet.synsets(word) or len(
                        word) < 2 or word.lower() in stopwords:  # 去除标点符号、特殊字符以及停用词
                    if not word in '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+':
                        word_temp2.append(word.lower())
                    continue
                dict[word] = pos
                word_temp.append(word)
            for j in range(temp_index, len(word_temp)):
                word_pos = dict[word_temp[j]]
                if word_pos.startswith('J'):
                    word_temp[j] = wordnet_lemmatizer.lemmatize(word_temp[j].lower(), pos=wordnet.ADJ)
                elif word_pos.startswith('V'):
                    word_temp[j] = wordnet_lemmatizer.lemmatize(word_temp[j].lower(), pos=wordnet.VERB)
                elif word_pos.startswith('N'):
                    word_temp[j] = wordnet_lemmatizer.lemmatize(word_temp[j].lower(), pos=wordnet.NOUN)
                    if (word_pos == 'NN' or word_pos == 'NNS' or word_pos == 'NNP' or word_pos == 'NNPS') and not \
                    word_temp[j] in stopwords2:
                        if wordnet.synsets(word_temp[j]) and len(word_temp[j]) > 1:
                            noun_set.add(word_temp[j])
                elif word_pos.startswith('R'):
                    word_temp[j] = wordnet_lemmatizer.lemmatize(word_temp[j].lower(), pos=wordnet.ADV)
                else:
                    word_temp[j] = wordnet_lemmatizer.lemmatize(word_temp[j].lower(), pos=wordnet.NOUN)
                temp_index = j + 1
        word_list.append(word_temp + word_temp2)
        noun_list.append(noun_set)
        noun_set_len = noun_set_len + len(noun_set)
        # print(noun_set)
    noun_set_len = math.floor(noun_set_len / len(noun_list))

    # 使用wordnet比较名词之间的相似度，求出每个名词在所在文档中的名词平均相似度
    sim_dict = {}  # 名词平均相似度词典
    sim_list = []  # 存放各描述文本名词平均相似度的数组
    noun_list2 = []  # 用于存放每条描述最终参与计算的功能名词
    for (temp_set, tag) in zip(noun_list, tag_str):
        for i in temp_set:
            # 初始化初始相似度
            simi = 0
            tsim = 0
            tagi = tag.split(",")
            for t in tagi:
                try:
                    t = wordnet_lemmatizer.lemmatize(t.strip().lower(), pos=wordnet.NOUN)
                    senst = wordnet.synset(t + '.n.1')
                    sensi = wordnet.synset(i + '.n.1')
                    sens_path = sensi.path_similarity(senst)
                    if (tsim < sens_path):
                        tsim = sens_path
                except:
                    continue
            for j in temp_set:
                if i == j:
                    continue
                try:
                    sensi = wordnet.synset(i + '.n.1')
                    sensj = wordnet.synset(j + '.n.1')
                    simi += sensi.path_similarity(sensj) / (len(temp_set) - 1)
                except:
                    continue
            if (len(temp_set)==noun_set_len):
                 w = 0.5
            else:
                 w=0.5/(abs(len(temp_set)-noun_set_len))
            sim_dict[i] = simi * w + tsim * (1 - w)
        temp_list = sorted(sim_dict.items(), key=lambda item: item[1], reverse=True)
        noun_set2 = set()  # 存放需最终计算的功能名词
        sim_dict = {}
        if len(temp_list) <= noun_set_len:
            for l in temp_list:
                sim_dict[l[0]] = l[1]
                noun_set2.add(l[0])
        else:
            index = 0
            while (index < noun_set_len):
                sim_dict[temp_list[index][0]] = temp_list[index][1]
                noun_set2.add(temp_list[index][0])
                index = index + 1
        sim_list.append(sim_dict)
        noun_list2.append(noun_set2)
        # print(sim_dict)
        sim_dict = {}

    # 赋给语料库中每个词(不重复的词)一个整数id
    dictionary = corpora.Dictionary(word_list)  # 建立词典
    # for key in dictionary.iterkeys():
    #      print (key,dictionary.get(key),dictionary.dfs[key])#查看字典主键、值以及频度
    # dictionary.doc2bow(doc)是把文档 doc变成一个稀疏向量，[(0, 1), (1, 1)]，表明id为0,1的词汇出现了1次
    new_corpus = [dictionary.doc2bow(text) for text in word_list]
    # print(new_corpus)

    # 训练tfidf模型
    tfidf = models.TfidfModel(new_corpus)
    tfidf.save("model.tfidf")
    # 载入tfidf模型
    tfidf = models.TfidfModel.load("model.tfidf")
    tfidf_vec = []
    for i in range(len(word_list)):
        string_bow = dictionary.doc2bow(word_list[i])
        string_tfidf = tfidf[string_bow]  # 取得每个词的tfidf值(以元组的形式)
        string_tfidf = sorted(string_tfidf, key=lambda item: item[1], reverse=True)  # 对元组的tfidf权值按降序进行排序
        tfidf_vec.append(string_tfidf)

    # 加载word2vec
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors300.bin', binary=True)
    # 遍历tfidf_vec,结合word2vec计算本文向量
    for (tfidf_list, n_set, sim_dic) in zip(tfidf_vec, noun_list2, sim_list):
        doc = np.zeros(300)
        doc = np.array(doc)
        for tfidf in tfidf_list:
            wv = np.zeros(300)
            try:
                wv = np.array(model[dictionary[tfidf[0]]])
            except KeyError:
                continue
            if dictionary[tfidf[0]] in n_set:
                ti = tfidf[1]
                word_sim = sim_dic[dictionary[tfidf[0]]]
                # 在n_set有多个名词的情况下，word_sim为0证明该词在描述中与其他名词无语义联系
                if word_sim == 0 and len(n_set) > 1:
                    ti = 0
                doc += wv * (ti / (1 - word_sim))
            else:
                continue
        doc_vec.append(doc)
    return doc_vec