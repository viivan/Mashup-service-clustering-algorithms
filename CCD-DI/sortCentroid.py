# 将初步质心按 密度*高密度距离 从大到小排序
def sortCentroid(preCentroid, dis, p):
    mul = {}
    Centroid = []
    for i in preCentroid:
        mul[i] = dis[i] * p[i]
    mul = list(mul.items())
    mul.sort(key=lambda x: x[1], reverse=True)
    for j in mul:
        Centroid.append(j[0])
    return Centroid