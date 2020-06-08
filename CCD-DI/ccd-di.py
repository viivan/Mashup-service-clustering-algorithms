#输入：语义特征向量相似度信息
#输出：得到的最优质心
def CCD_DI(result):
    p = {}  # 密度
    # 遍历excel表，得到数据集
    total = gettotal()


    # 获取局部密度
    lD = localDensity(result, total, p, 10)


    # 获取高密度距离
    dis = getDis(lD, result)


    radius, online_tup = neighborhood_sizes(dis)


    # 排除异常点，得到初步质心
    preCentroid = getpreCentroid(total, result, online_tup, radius)


    # 将初步质心按 密度*高密度距离 从大到小排序
    preCentroid = sortCentroid(preCentroid, dis, p)


    # 找到最终质心
    finalCentroid = getfinalCentroid(preCentroid, dis, p, result, radius, total)


