# kMeans聚类函数
# 输入：初始质心、特征向量数组等
# 输出：聚类结果
def kMeans(centroids, total, result, doc_vec):
    time = 1
    k = len(centroids)
    size = len(total)
    # zeros给数值赋初始值；mat生成矩阵，为字符串或列表形式以，隔开
    clusterAssment = np.mat(np.zeros((size, 2)))  # 创建两列的矩阵，用来保存簇分配结果
    clusterChanged = True  # 判断所有点所归属的质心是否改变
    while clusterChanged:
        clusterChanged = False
        for i in range(size):  # 循环每一个数据点并分配到最近的质心中去
            maxSim = 0
            maxIndex = -1
            for j in range(k):
                if centroids[j] == total[i]:
                    clusterAssment[i, :] = total[i], total[i]
                    maxIndex = clusterAssment[i, 0]
                    break
                else:
                    if total[i] > centroids[j]:
                        s = str(centroids[j]) + '-' + str(total[i])
                    else:
                        s = str(total[i]) + '-' + str(centroids[j])
                    similarity = result[s]  # 计算数据点到质心的距离
                    if similarity > maxSim:
                        maxSim = similarity
                        maxIndex = centroids[j]
            if clusterAssment[i, 0] != maxIndex:  # 簇分配结果改变
                clusterChanged = True  # 簇改变
                clusterAssment[i, :] = maxIndex, total[i]  # 更新索引
        mul_centroids = []
        for cent in range(k):
            c = []
            # 显示每一次聚类结果
            for j in range(len(clusterAssment)):
                if clusterAssment[j, 0] == centroids[cent]:
                    c.append(int(clusterAssment[j, 1]))
            print(c)
            # 更新质心
            ptsInClust = c
            average_doc = np.zeros(300)
            average_doc = np.array(average_doc)
            # 计算平均文本向量
            for i in ptsInClust:
                average_doc += doc_vec[i]
            average_doc = average_doc / len(ptsInClust)
            maxSim = 0
            maxIndex = -1
            for i in ptsInClust:
                sim = compute(doc_vec[i],average_doc)
                if sim > maxSim:
                    maxSim = sim
                    maxIndex = i
            mul_centroids.append(maxIndex)  # 将质心修改为簇中所有点的文本向量的平均值
        time += 1
        centroids = mul_centroids
    return centroids, clusterAssment