# LDA主题向量
def kMeans(X,K):
    ldaModel = lda.LDA(n_topics=K, n_iter=1500, random_state=1)
    ldaModel.fit(X)
    theta = ldaModel.doc_topic_
    return theta