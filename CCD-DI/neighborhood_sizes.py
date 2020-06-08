# 计算邻域集合
def neighborhood_sizes(dis)
    temp = dis
    dis = list(dis.items())
    dis.sort(key=lambda x x[1], reverse=False)
    min = dis[0][1]  # 最小的距离值
    max = dis[-1][1]  # 最大的距离值
    bound = (max + min)  2  # 邻域半径的上界
    sum = 0  # 高密度距离差值的和
    under_mid = []  # 在上界以下的点
    for i in dis
        if i[1]  bound
            under_mid.append(i[0])
    k = 0
    for i in under_mid
        for j in under_mid
            if not i == j
                if i  j
                    s = str(j) + '-' + str(i)
                else
                    s = str(i) + '-' + str(j)
                sum += abs(temp[i] - temp[j])
                k += 1
    t = sum  k  # 上界下所有点高密度差值的平均值作为半径的初始值
    t1 = 0
    t2 = t
    pre_inc = 0
    radius = bound
    while t1  bound
        a = []
        for i in dis
            if i[1] = t1 and i[1]  t2
                a.append(i[0])
        now_inc = len(a)
        if now_inc  pre_inc
            radius = t1
            break
        else
            pre_inc = now_inc
        t1 = t2
        t2 += t
    for i in range(0, len(dis))
        if dis[i][1]  radius
            return radius, dis[i]  # 返回邻域半径和线上点的集合