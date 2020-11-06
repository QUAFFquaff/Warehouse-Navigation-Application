def direction(data, start_point, end_point, result) -> list:
    """

    :return: text str list
    :param data: loaded data
    :param start_point:
    :param end_point:
    :param result: shortest path result
    """
    id_dictionary = []
    x_dictionary = []
    y_dictionary = []
    route = []
    for i in range(len(data)):
        id_dictionary.append(int(data[i][0]))
        x_dictionary.append(data[i][1])
        y_dictionary.append(data[i][2])
    path = result['path']
    # print(path)
    x_axis = x_dictionary[path[1] - 1] - start_point[0]
    y_axis = y_dictionary[path[1] - 1] - start_point[1]
    description_str = "From Start Point to Product {}, moving x-direction {}, moving y-direction {}\n".format(
        id_dictionary[path[1] - 1], format(x_axis, '.2f'), format(y_axis, '.2f'))
    route.append(description_str)

    for i in range(1, len(path) - 2):
        prev_point = id_dictionary[path[i] - 1]
        next_point = id_dictionary[path[i + 1] - 1]
        x_axis = x_dictionary[path[i+1] - 1] - x_dictionary[path[i] - 1]
        y_axis = y_dictionary[path[i+1] - 1] - y_dictionary[path[i] - 1]
        description_str = "From Product {} to Product {}, moving x-direction {}, moving y-direction {}\n".format(
            prev_point, next_point, format(x_axis, '.2f'), format(y_axis, '.2f'))
        route.append(description_str)
    x_axis = end_point[0] - x_dictionary[path[len(path) - 2] - 1]
    y_axis = end_point[1] - y_dictionary[path[len(path) - 2] - 1]
    description_str = "From Product {} to End Point, moving x-direction {}, moving y-direction {}\n".format(
        id_dictionary[path[len(path) - 2] - 1], format(x_axis, '.2f'), format(y_axis, '.2f'))
    route.append(description_str)
    return route
