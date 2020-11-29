import utils.LoggerFactory as LF
from algorithm.Astar import *

smtplogger = LF.get_logger(__name__)


def show_me_the_path(result, path_list, plist, maze):
    plist_temp = plist[:]
    plist_temp.insert(0, 0)
    plist_temp.append(25526)
    order = []
    for i, val in enumerate(result):
        order.append(plist_temp.index(val))
    # smtplogger.info('order {}'.format(order))
    path_dot = []
    out = []
    for j in range(len(plist_temp) - 1):
        smtplogger.info('new episode')
        out.append(path_list[(order[j] * len(plist_temp)) + (order[j + 1])])
        for k in path_list[(order[j] * len(plist_temp)) + (order[j + 1])]:
            path_dot.append(k)
        print_map(path_dot, maze)
        smtplogger.info("from {} to {}".format(result[j], result[j + 1]))
        smtplogger.info(path_list[(order[j] * len(plist_temp)) + (order[j + 1])])

    smtplogger.info("path_dot{}".format(path_dot))
    smtplogger.info('total dis {}'.format(len(path_dot) - len(plist) - 1))

    return path_dot, out
