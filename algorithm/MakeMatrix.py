
import numpy as np
from objs.WareHouse import *
from objs.DataHandler import *


def MakeMatrix(data, order_list) -> dict:

    """
    :param data: data from txt
    :param order_list: random generated, value in order_list represents the # of an item, NOT PRODUCT ID
            Product id can be retrieved by id_dictionary
    :return: x matrix and y matrix
    """

    id_dictionary = []
    position_dictionary = []
    #print(order_list)

    order_list_temp = order_list[:]

    #print(order_list_temp)

    for i in range(len(data)):
        position_temp = []
        id_dictionary.append(int(data[i][0]))
        position_temp.append(data[i][1])
        position_temp.append(data[i][2])
        position_dictionary.append(tuple(position_temp))

    #print(id_dictionary)
    start_point = (0.0, 0.0)
    end_point = (0.0, 0.0)
    position_dictionary.insert(0, start_point)
    position_dictionary.append(end_point)

    order_list_temp.insert(0, 0)
    order_list_temp.append(len(position_dictionary) - 1)
    print(order_list_temp)

    x = np.zeros(shape=(len(order_list_temp), len(order_list_temp)))
    y = np.zeros(shape=(len(order_list_temp), len(order_list_temp)))

    for i, val_i in enumerate(order_list_temp):
        for j, val_j in enumerate(order_list_temp[i + 1:], i + 1):
            x[i][j] = abs(position_dictionary[val_j][0] - position_dictionary[val_i][0])
            y[i][j] = abs(position_dictionary[val_j][1] - position_dictionary[val_i][1])

    x = x + x.T
    y = y + y.T

    return {'xmatrix': x, 'ymatrix': y}



