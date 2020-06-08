# 检测出最终质心
def getfinalCentroid(preCentroid, dis, p, result, radius, total):
    N = 0  # 全局中心点（ρ×δ值最大）在半径领域（最后红线的高度即半径）内包含的点数

    for j in total:
        if not preCentroid[0] == j:
            if preCentroid[0] > j:
                s = str(j) + '-' + str(preCentroid[0])
            else:
                s = str(preCentroid[0]) + '-' + str(j)
            if 1 - result[s] < radius:
                N += 1

    neighbourhood = {}  # 初步质心邻域中最近的前 N 个点
    for i in preCentroid:
        t = {}
        a = []
        for j in total:
            if not i == j:
                if i > j:
                    s = str(j) + '-' + str(i)
                else:
                    s = str(i) + '-' + str(j)
                t[j] = 1 - result[s]
        t = list(t.items())
        t.sort(key=lambda x: x[1], reverse=False)
        for k in t[0:N]:
            a.append(k[0])
        neighbourhood[i] = a
    sigma = {}  # 对排除异常点后筛选的剩余点求离它们最近的N个点的ρ×δ的波动值
    for k, v in neighbourhood.items():
        s = 0
        avg = 0
        for i in v:
            avg += dis[i] * p[i] / len(v)
        for j in v:
            s += (dis[j] * p[j] - avg) ** 2 / len(v)
        s = s ** 0.5
        sigma[k] = s

    sortsigma = list(sigma.items())
    sortsigma.sort(key=lambda x: x[1], reverse=True)
    sigma_max = sortsigma[0][1]
    sigma_min = sortsigma[-1][1]

    mul = {}
    for i in preCentroid:
        mul[i] = dis[i] * p[i]
    mul = list(mul.items())
    mul.sort(key=lambda x: x[1], reverse=True)
    mul_max = mul[0][1]
    mul_min = mul[-1][1]

    Eva = {}  # 评价方式
    for i in preCentroid:
        w = 0.5
        Eva[i] = (1 - w) * ((p[i] * dis[i] - mul_min) / (mul_max - mul_min)) + w * (
                    1 - ((sigma[i] - sigma_min) / (sigma_max - sigma_min)))
    Eva = list(Eva.items())
    Eva.sort(key=lambda x: x[1], reverse=True)
    res_list = [x[0] for x in Eva]
    return res_list[0:10]