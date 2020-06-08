# 计算局部密度
def localDensity(result, total, p, num):
    k = num  # 距离数据点最近的点的个数
    temp = []  # 用来存放数据点相似度
    lD = []  # lD中存放数据点的局部密度
    for i in total:
        p[i] = 0
        for j in total:
            if not i == j:
                if i > j:
                    s = str(j) + '-' + str(i)
                else:
                    s = str(i) + '-' + str(j)
                temp.append(result[s])
        # 将相似度最大的前k为相加，作为数据点的局部密度
        temp.sort(reverse=True)
        p[i] += sum(temp[:k])
        temp[::] = []
    lD = list(p.items())
    lD.sort(key=lambda x: x[1], reverse=True)
    return lD