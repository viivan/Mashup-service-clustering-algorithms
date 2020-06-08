# 计算高密度距离
def getDis(lD, result):
    min = 1  # 高密度距离的上限是1
    dis = {}
    for i in range(len(lD)):
        if i == 0:  # 计算密度最大的点的高密度距离
            for j in range(len(lD)):
                if j == 0:
                    continue
                else:
                    if lD[0][0] > lD[j][0]:
                        s = str(lD[j][0]) + '-' + str(lD[0][0])
                    else:
                        s = str(lD[0][0]) + '-' + str(lD[j][0])
                    if result[s] < min:
                        min = result[s]
            dis[lD[0][0]] = 1 - min
        else:  # 计算剩余点的高密度距离
            max = 0  # 高密度距离的下限是0
            for j in range(0, i):
                if lD[i][0] > lD[j][0]:
                    s = str(lD[j][0]) + '-' + str(lD[i][0])
                else:
                    s = str(lD[i][0]) + '-' + str(lD[j][0])
                if result[s] > max:
                    max = result[s]
            dis[lD[i][0]] = 1 - max
    return dis