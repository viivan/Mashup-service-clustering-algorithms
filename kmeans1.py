def k_cluster(doc_vec, K):  
    e = KMeans(n_clusters=K,init='random').fit(doc_vec)
    label = e.labels_
    
    #返回分类标签
    return label