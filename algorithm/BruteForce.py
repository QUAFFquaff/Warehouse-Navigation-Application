import itertools


def brute_force(m, d_matrix, source, target, plist):
    """
    :param plist: product list
    :param m: subprocess output message
    :param d_matrix: x+y
    :param source: start point
    :param target: target point, usually source and target are the same
    """

    perm = itertools.permutations(plist, len(plist))
    # print(perm)
    # print(len(perm))

    temp1 = plist[:]
    temp1.insert(0, source)
    temp1.append(target)

    min_dist = float('Inf')

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
            min_path = list(item)
            m['path'] = min_path
            m['distance'] = min_dist
