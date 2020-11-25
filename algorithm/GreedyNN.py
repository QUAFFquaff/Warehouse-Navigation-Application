def greedy_nn(d_matrix, source, target, plist) -> dict:
    """

    :param d_matrix:
    :param source:
    :param target:
    :param plist:
    :return: path and distance
    """
    temp = plist[:]
    # print('pl',plist)
    temp.insert(0, source)
    temp.append(target)

    pop_list = []
    path_list = [0]

    d = 0
    prev = 0
    for k in range(len(plist)):
        nnl = list(d_matrix[prev])

        pop_temp = pop_list[:]
        # print('nnl',nnl)
        pop_temp.append(prev)
        pop_temp.append(len(temp) - 1)  # last one
        # print('pt',pop_temp)

        nnl_trim = [j for i, j in enumerate(nnl) if i not in pop_temp]

        # print('nnd_trim',nnl_trim)
        d = d + min(nnl_trim)
        path_list.append(temp[list(d_matrix[prev]).index(min(nnl_trim))])
        pop_list.append(prev)
        prev = list(d_matrix[prev]).index(min(nnl_trim))
        # print(path_list,pop_list,d)
    d = d + d_matrix[prev][len(temp) - 1]
    path_list.append(target)

    res = {'path': path_list, 'distance': d}
    return res
