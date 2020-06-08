#tfidf向量模型
#输入：各服务的描述文本
#输出：各服务的tfidf特征向量
def tfidf(line_str):
    doc_vec =[]
    corpus = []
    for line in line_str:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        corpus.append(line_seg)
    tfidf_model = TfidfVectorizer()
    corpus_tfidf = tfidf_model.fit_transform(corpus)
    tfidf_arr = corpus_tfidf.toarray()
    for tfidf in tfidf_arr:
        doc_vec.append(tfidf)
    return doc_vec