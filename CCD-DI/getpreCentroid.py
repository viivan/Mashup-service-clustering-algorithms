# 排除异常点，获取初步质心
def getpreCentroid(total, result, online_tup, radius):
    preCentroid = []
    for i in online_tup:
        for j in total:
            if not i[0] == j:
                if i[0] > j:
                    s = str(j) + '-' + str(i[0])
                else:
                    s = str(i[0]) + '-' + str(j)
                if 1 - result[s] < radius:
                    preCentroid.append(i[0])
                    break
    return preCentroid