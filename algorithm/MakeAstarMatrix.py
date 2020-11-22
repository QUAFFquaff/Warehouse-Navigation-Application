import numpy as np
import math
from algorithm.Astar import *

import utils.LoggerFactory as LF


mamlogger = LF.get_logger(__name__)


def make_astar_matrix(data, maze, start_point, end_point, order_list) -> dict:
    """
    :param end_point:
    :param start_point:start_point = (x,y)
    :param data: data from txt
    :param order_list: random generated, value in order_list represents the # of an item, NOT PRODUCT ID
            Product id can be retrieved by id_dictionary
    :return: x matrix and y matrix
    """

    # floor start/end point
    start_point_floor =[0,0]
    end_point_floor = [0,0]
    start_point_floor[0] = math.floor(start_point[0])
    start_point_floor[1] = math.floor(start_point[1])
    end_point_floor[0] = math.floor(end_point[0])
    end_point_floor[1] = math.floor(end_point[1])
    start_point_floor = tuple(start_point_floor)
    end_point_floor = tuple(end_point_floor)
    mamlogger.info("s/e {}".format(start_point_floor, end_point_floor))

    id_dictionary = []
    position_dictionary = []
    # print(order_list)

    order_list_temp = order_list[:]

    # print(order_list_temp)
########### four direction +1########
    for i in range(len(data)):
        position_temp = []
        id_dictionary.append(int(data[i][0]))
        position_temp.append(math.floor(data[i][2]))
        position_temp.append(math.floor(data[i][1])+1)
        position_dictionary.append(tuple(position_temp))

    # print(id_dictionary)
    #start_point = (0.0, 0.0)
    #end_point = (0.0, 0.0)
    position_dictionary.insert(0, start_point_floor)
    position_dictionary.append(end_point_floor)

    order_list_temp.insert(0, 0)
    order_list_temp.append(len(position_dictionary) - 1)
    mamlogger.info("orderlist(rank) {}".format(order_list_temp))

    ##################
    plist_position = []
    for i in order_list_temp:
        plist_position.append(position_dictionary[i])
    mamlogger.info("plistposi {}".format(plist_position))
    ##############

    distance_matrix = np.zeros(shape=(len(order_list_temp), len(order_list_temp)))
    path_matrix = np.zeros(shape=(len(order_list_temp), len(order_list_temp)))

    for i, val_i in enumerate(order_list_temp):
        for j, val_j in enumerate(order_list_temp[i + 1:], i + 1):
            mamlogger.info("from {} to {}".format(position_dictionary[val_i], position_dictionary[val_j]))
            distance_matrix[i][j] = len(astar(maze, position_dictionary[val_i], position_dictionary[val_j]))-1
            #path_matrix[i][j] = Astar.astar(maze, position_dictionary[val_i], position_dictionary[val_j])
            #print(path_matrix)
            #distance_matrix[i][j] = Astar.example(maze, position_dictionary[val_i], position_dictionary[val_j])
                #abs(position_dictionary[val_j][0] - position_dictionary[val_i][0])
            #y[i][j] = abs(position_dictionary[val_j][1] - position_dictionary[val_i][1])

    distance_matrix = distance_matrix + distance_matrix.T
    #y = y + y.T

    #return {'xmatrix': x, 'ymatrix': y}
    return distance_matrix




