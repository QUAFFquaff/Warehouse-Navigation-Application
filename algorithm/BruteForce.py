import numpy as np
import itertools


def brute_force(x_matrix,y_matrix,d_matrix,source,target,plist)->dict:

    """
    :param plist: product list
    :param x_matrix: x difference
    :param y_matrix: y-dimensional difference
    :param d_matrix: x+y
    :param source: start point
    :param target: target point, usually source and target are the same
    :return: result dict
    """

    print('in')
    dlist = []
    perm = list(itertools.permutations(plist, len(plist)))


    for i in range(len(perm)):
        d = 0
        temp = list(perm[i])

        temp.insert(0, source)
        temp.append(target)
        #print(temp)

        for j in range(len(temp)-1):
            #print(temp[j])
            d = d+d_matrix[temp[j]][temp[j+1]]
            #print(d)
        dlist.append(d)

    index_min = np.argmin(dlist)
    path_min = min(dlist)

    temp_path = list(perm[index_min])
    temp_path.insert(0,source)
    temp_path.append(target)
    res = {'path': temp_path, 'distance': path_min}

    return res





