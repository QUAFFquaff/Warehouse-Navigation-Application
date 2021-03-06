import os
import objs.DataHandler as DataHandler
import objs.Products as Products
import objs.Order as Order
import time
from enum import Enum
from algorithm.BruteForce import *
from algorithm.Direction import direction
from algorithm.MakeMatrix import *
from algorithm.algorithms import *
from algorithm.MakeMaze import *
from algorithm.MakeAstarMatrix import *
from algorithm.ShowMeThePath import *
from algorithm.GreedyNN import *

from objs.DataHandler import *

Rule = Enum('Rule', ('Branch_and_bound', 'Greedy_nn'))
import utils.LoggerFactory as LF
from multiprocessing import Process, Manager

import time


class WareHouse:
    def __init__(self, worker=None, orders=[], dhandler=None):
        self.logger = LF.get_logger(__name__)
        self.worker = worker
        self.orders = orders
        self.dhandler = dhandler
        self.products = []
        self.rules = Rule.Branch_and_bound
        self.data = None
        self.start_point = (0.0, 0.0)
        self.end_point = (0.0, 0.0)
        self.products_index_of_one_order_in_data = []
        self.id_to_ind_dict = {}
        self.timeout = 60
        self.shelf_list = []
        self.allow_diagonal_movement = False
        self.f = None

    def set_rules(self, num):
        if num == 0:
            self.rules = Rule.Branch_and_bound
        elif num == 1:
            self.rules = Rule.Greedy_nn

    def set_dhandler(self):
        self.dhandler = DataHandler()

    def set_orders(self):
        self.orders = Order.Order(time.time())

    def add_order(self, num, p_list=None):
        if not p_list:
            order = Order.Order(time.time())
            inds = order.init_products(num, self.products)
        else:
            order = Order.Order(time.time())
            p_list = list(map(int, p_list))

            print('p_list', p_list)
            p_list_ind = []
            for i in range(len(p_list)):
                if self.id_to_ind_dict.get(p_list[i]) is None:
                    logger.error("Product id {} not found!".format(p_list[i]))
                    raise Exception("Product id not found!")
                p_list_ind.append(self.id_to_ind_dict[p_list[i]])
            inds = order.add_products(p_list_ind, self.products)
            print('inds', inds)
            print('p_list_ind', p_list_ind)
        self.products_index_of_one_order_in_data.append(inds)
        self.orders.append(order)

        img_name = "data/path/dot.html"
        p_nodes = []
        for i in inds:
            p = self.products[i]
            print(p)
            p_nodes.append([p.get_id(), p.x, p.y])
        print(p_nodes)
        draw_dots_html(self.shelf_list, p_nodes, img_name)
        return inds

    def load_orders(self, filename):

        orders = self.dhandler.load_orders(filename)

        for o in orders:
            logger.info("loading orders  {}".format(o))
            p_list = list(map(int, o))
            inds = [self.id_to_ind_dict[i] for i in p_list]
            order = Order.Order(time.time())
            order.add_products(inds, self.products)
            self.products_index_of_one_order_in_data.append(inds)
            self.orders.append(order)
        logger.info("loading orders from {}".format(filename))

    def generate_path(self, order, index):
        '''
        :param order:
        :param index: index of the order in all orders
        :return:
        '''
        #################
        ### TEST ONLY ###
        #################
        start_time = time.time()

        # print("index: ",index)
        products_index_of_one_order_in_data = [i + 1 for i in self.products_index_of_one_order_in_data[index]]
        print("products_index_of_one_order_in_data: ", products_index_of_one_order_in_data)
        logger.info("products_index_of_one_order_in_data: {}".format(products_index_of_one_order_in_data))

        pro_list = [[p.get_id(), p.x, p.y] for p in order.products]

        maze1 = make_maze(self.data)
        d, path_list = make_astar_matrix(self.data, maze1, self.start_point, self.end_point,
                                         products_index_of_one_order_in_data, self.allow_diagonal_movement)
        print(d)
        if self.rules == Rule.Branch_and_bound:
            self.logger.info("using branch and bound")

            sourcetest = 0
            targettest = len(self.data) + 1

            manager = Manager()
            m = manager.dict()
            p1 = Process(target=brute_force, args=(m, d, sourcetest, targettest, products_index_of_one_order_in_data),
                         name='process 1')
            p1.start()
            p1.join(timeout=self.timeout)
            p1.terminate()
            logger.info("m['path']: {}".format(m['path']))

            route1 = []
            path_copy = m['path'].copy()
            path_dot, out = show_me_the_path(m['path'], path_list, products_index_of_one_order_in_data, maze1)
            for i, p in enumerate(out):
                if i == 0:
                    part_res = (self.start_point, int(self.data[path_copy[1] - 1][0]))
                    print(part_res)
                elif i == len(path_copy) - 2:
                    part_res = (int(self.data[path_copy[i] - 1][0]), self.end_point)
                else:
                    part_res = (int(self.data[path_copy[i] - 1][0]), int(self.data[path_copy[i + 1] - 1][0]))
                route1.append((part_res, p))


            #################
            ### TEST ONLY ###
            #################
            '''
            end_time = time.time()
            path_result_id = []
            for i, step in enumerate(m['path']):
                if i != 0 and i != len(m['path']) - 1:
                    path_result_id.append(int(self.data[step-1][0]))
                else:
                    pass
            print("REPORT BF\nOrder[{}]\ntotal running time {} s\nresult path is{}\ntotal distance: {}".format(order.to_string(),
                                                                                                    end_time - start_time,
                                                                                                    path_result_id,
                                                                                                    m['distance']))
            '''

            end_time = time.time()
            path_result_id = []
            for i, step in enumerate(m['path']):
                if i != 0 and i != len(m['path']) - 1:
                    path_result_id.append(int(self.data[step-1][0]))
                else:
                    pass
            print("REPORT BF\nOrder[{}]\ntotal running time {} s\nresult path is{}\ntotal distance: {}".format(order.to_string(),
                                                                                                    end_time - start_time,
                                                                                                    path_result_id,
                                                                                                    m['distance']))

            self.logger.info("brute force result(path): {}".format(m["path"]))
            self.logger.info("pro_list: {}".format(pro_list))
            # draw_png_graph(pro_list, m['path'])
            file_name = 'data/path/path.html'
            draw_path_html(self.shelf_list, pro_list, path_dot, file_name)

            self.logger.info("finish generating path")
            return route1
        if self.rules == Rule.Greedy_nn:
            self.logger.info("using greedy nn")

            sourcetest = 0
            targettest = len(self.data) + 1

            res = greedy_nn(d, sourcetest, targettest, products_index_of_one_order_in_data)

            route1 = []
            path_copy = res['path'].copy()
            path_dot, out = show_me_the_path(res['path'], path_list, products_index_of_one_order_in_data, maze1)

            for i, p in enumerate(out):
                if i == 0:
                    part_res = (self.start_point, int(self.data[path_copy[1] - 1][0]))
                    print(part_res)
                elif i == len(path_copy) - 2:
                    part_res = (int(self.data[path_copy[i] - 1][0]), self.end_point)
                else:
                    part_res = (int(self.data[path_copy[i] - 1][0]), int(self.data[path_copy[i + 1] - 1][0]))
                route1.append((part_res, p))

            file_name = 'data/path/path.html'
            draw_path_html(self.shelf_list, pro_list, path_dot, file_name)

            #################
            ### TEST ONLY ###
            #################
            '''
            end_time = time.time()
            path_result_id = []
            for i, step in enumerate(res['path']):
                if i != 0 and i != len(res['path']) - 1:
                    path_result_id.append(int(self.data[step-1][0]))
                else:
                    pass
            print("REPORT NN\nOrder[{}]\ntotal CPU running time {} s\nresult path is{}\ntotal distance: {}\n".format(
                order.to_string(), end_time - start_time, path_result_id, res['distance']))

            '''
            end_time = time.time()
            path_result_id = []
            for i, step in enumerate(res['path']):
                if i != 0 and i != len(res['path']) - 1:
                    path_result_id.append(int(self.data[step-1][0]))
                else:
                    pass
            print("REPORT NN\nOrder[{}]\ntotal CPU running time {} s\nresult path is{}\ntotal distance: {}\n".format(
                order.to_string(), end_time - start_time, path_result_id, res['distance']))

            return route1

        self.logger.info("finish generating path")

    def load_data(self, path):
        self.data = self.dhandler.load_txt(path)
        for ind, d in enumerate(self.data):
            product = Products.Product(int(d[0]), d[1], d[2])
            self.products.append(product)
            self.id_to_ind_dict[d[0]] = ind

        pro_list = [[p.get_id(), p.x, p.y] for p in self.products]
        # draw_warehouse(pro_list,"data/path/warehouse.png")

        dot_list = []
        for p in pro_list:
            temp = [int(p[1]), int(p[2])]
            if temp not in dot_list:
                dot_list.append(temp)
        self.shelf_list = dot_list
        if not os.path.exists("data/path"):
            os.makedirs("data/path")
        draw_warehouse_html(self.shelf_list, "data/path/warehouse.html")

    def get_string_list_orders(self):
        orders = []
        for order in self.orders:
            orders.append(order.to_string())
        return orders

    def __del__(self):
        if self.f is not None:
            unfinished_orders = []
            for order in self.orders:
                order_list = []
                for p in order.products:
                    order_list.append(p.get_id())
                unfinished_orders.append(order_list)
            path = 'data/unfinished_orders.txt'
            self.dhandler.save_orders(unfinished_orders,path,self.f)
            self.f.close()
