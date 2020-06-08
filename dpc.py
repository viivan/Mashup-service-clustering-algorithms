# 直接利用初始聚类中心输出聚类结果
#输入：初始聚类中心
#输出：DPC聚类结果
def simple_cluster(centroids, total, result, doc_vec):
    time = 1
    k = len(centroids)
    size = len(total)

    # zeros给数值赋初始值；mat生成矩阵，为字符串或列表形式以，隔开
    clusterAssment = np.mat(np.zeros((size, 2)))  # 创建两列的矩阵，用来保存簇分配结果
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
                # 找到相似度最高的簇中心，将当前元素分入
                if similarity > maxSim:
                    maxSim = similarity
                    maxIndex = centroids[j]
            if clusterAssment[i, 0] != maxIndex:  # 簇分配结果改变
                clusterAssment[i, :] = maxIndex, total[i]  # 更新索引
    return clusterAssment