import numpy as np
import math


def make_maze(data):
    datanp = np.array(data)

    row = math.ceil(datanp.max(axis=0, initial=-1)[2])
    column = math.ceil(datanp.max(axis=0, initial=-1)[1])

    maze = np.zeros((row + 3, column + 2))
    # print(maze)
    for i in range(len(data)):
        y = math.floor(data[i][2])
        x = math.floor(data[i][1])
        maze[y + 1][x + 1] = 1
    # print(maze)
    return maze
