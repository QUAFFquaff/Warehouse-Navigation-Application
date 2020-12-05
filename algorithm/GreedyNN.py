def greedy_nn(d_matrix, source, target, plist) -> dict:
    """

    :param d_matrix:
    :param source:
    :param target:
    :param plist:
    :return: path and distance
    """
    temp = plist[:]
    temp.insert(0, source)
    temp.append(target)
    d_min = float('inf')
    # print('d_min ', d_min)

    for p in range(len(plist)):
        pop_list = []
        path_list = [0]

        d = d_matrix[0][p + 1]
        prev = p + 1
        pop_list.append(0)
        pop_list.append(len(temp) - 1)  # last one
        # print(pop_list)
        for k in range(len(plist)):
            nnl = list(d_matrix[prev])

            nnl_trim = [j for i, j in enumerate(nnl) if i not in pop_list]
            # print(nnl,nnl_trim)
            d = d + min(nnl_trim)

            id1 = [i for i, x in enumerate(nnl) if x == min(nnl_trim)]
            id2 = [y for j, y in enumerate(id1) if y not in pop_list]
            path_list.append(temp[id2[0]])
            prev = id2[0]
            pop_list.append(prev)

        d = d + d_matrix[prev][len(temp) - 1]
        path_list.append(target)
        # print("path list", path_list)
        # print("d ", d)
        if d < d_min:
            d_min = d
            res = {'path': path_list, 'distance': d}
    # print(res)
    return res
