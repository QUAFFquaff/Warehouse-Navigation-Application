import itertools


def brute_force(m, d_matrix, source, target, plist):
    """
    :param plist: product list
    :param m: subprocess output message
    :param d_matrix: x+y
    :param source: start point
    :param target: target point, usually source and target are the same
    """
    temp1 = plist[:]
    temp1.insert(0, source)
    temp1.append(target)
    min_dist = float('Inf')

    # retrieve one item path
    if len(plist) == 1:
        min_dist = d_matrix[0][1]+d_matrix[1][2]
        # print(d_matrix[0][1], d_matrix[1][2])
        m['path'] = temp1
        m['distance'] = min_dist
        return

    perm = itertools.permutations(plist, len(plist))
    # print(perm)
    # print(len(perm))

    for item in perm:
        d = 0
        temp = list(item)

        temp.insert(0, source)
        temp.append(target)
        # print(temp)
        #print(item)

        for j in range(len(temp) - 1):
            # print(temp[j])
            d = d + d_matrix[temp1.index(temp[j])][temp1.index(temp[j + 1])]
            # print(temp1.index(temp[j]),temp1.index(temp[j+1]))
            # print(d)
        if d < min_dist:
            min_dist = d
            m['path'] = temp
            m['distance'] = min_dist
            
            
