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

Rule = Enum('Rule', ('Brute_force', 'Greedy_nn'))
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
        self.rules = Rule.Brute_force
        self.data = None
        self.order_listtest = []
        self.start_point = (0.0, 0.0)
        self.end_point = (0.0, 0.0)
        self.products_index_of_one_order_in_data = []
        self.id_to_ind_dict = {}
        self.timeout=60
        self.shelf_list = []

    def set_rules(self, num):
        if num == 0:
            self.rules = Rule.Brute_force
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
            p_list = list(map(int,p_list))
            for i in range(len(p_list)):
                if self.id_to_ind_dict.get(p_list[i]) is None:
                    logger.error("Product id {} not found!".format(p_list[i]))
                    raise Exception("Product id not found!")
                p_list[i]=self.id_to_ind_dict[p_list[i]]
            inds = order.add_products(p_list,self.products)
        self.order_listtest.append(inds)
        self.products_index_of_one_order_in_data.append(inds)
        self.orders.append(order)

        img_name = "data/path/dot.html"
        p_nodes = []
        for i in inds:
            p = self.products[i]
            print(p)
            p_nodes.append([p.get_id(),p.x,p.y])
        print(p_nodes)
        draw_dots_html(self.shelf_list,p_nodes,img_name)
        return inds

    def load_orders(self,filename):

        orders = self.dhandler.load_orders(filename)
        for o in orders:
            self.orders.append(o)
        logger.info("loading orders from {}".format(filename))

    def generate_path(self,order,index):
        '''

        :param order:
        :param index: index of the order in all orders
        :return:
        '''

        #TEST ONLY
        #start_time = time.time()

        products_index_of_one_order_in_data = self.products_index_of_one_order_in_data[index]
        logger.info("products_index_of_one_order_in_data: {}".format(products_index_of_one_order_in_data))

        pro_list = [[p.get_id(), p.x, p.y] for p in order.products]
     #############
        #ret = make_matrix(self.data, self.start_point, self.end_point, products_index_of_one_order_in_data)

        #d = ret['xmatrix'] + ret['ymatrix']
     #############
        maze1 = make_maze(self.data)
        d, path_list = make_astar_matrix(self.data, maze1, self.start_point, self.end_point, products_index_of_one_order_in_data)
        print(d)
        if self.rules == Rule.Brute_force:
            self.logger.info("using brute force")
            temp = [i + 1 for i in range(len(pro_list))]

            sourcetest = 0
            targettest = len(self.data)+1
            #print("data ",targettest)
            manager = Manager()
            m = manager.dict()
            p1 = Process(target=brute_force, args=(m, d, sourcetest, targettest, products_index_of_one_order_in_data),
                         name='process 1')
            p1.start()
            p1.join(timeout=self.timeout)
            p1.terminate()
            logger.info("m['path']: {}".format(m['path']))

            #### maze !!!
            #route1 = show_me_the_path(m['path'], path_list, products_index_of_one_order_in_data,maze1)

            #route = direction(self.data, self.start_point, self.end_point, m)
            route1 = []
            path_copy = m['path'].copy()
            for i, p in enumerate(show_me_the_path(m['path'], path_list, products_index_of_one_order_in_data, maze1)):
                if i == 0:
                    part_res = (self.start_point,int(self.data[path_copy[1]-1][0]))
                    print(part_res)
                elif i == len(path_copy)-2:
                    part_res = (int(self.data[path_copy[i]-1][0]),self.end_point)
                else:
                    part_res = (int(self.data[path_copy[i]-1][0]),int(self.data[path_copy[i+1]-1][0]))
                route1.append("({}, {})".format(part_res,p))

                #route1.append("({},{})".format(p[0],p[1]))
            #print(route1)
            # FOR TEST ONLY
            """
            end_time = time.time()
            path_result_id = []
            for i, step in enumerate(m['path']):
                if i != 0 and i != len(m['path'])-1:
                    path_result_id.append(int(self.data[step][0]))
                else:
                    pass
            print("Order[{}] total running time {}s result path is{}".format(order.to_string(),end_time-start_time,path_result_id))

            """


            ############################
            self.logger.info("brute force result(path): {}".format(m["path"]))
            # self.logger.info("draw png graph")
            # self.logger.info("pro_list: {}".format(pro_list))
            # draw_png_graph(pro_list, m['path'])
            self.logger.info("finish generating path")
            return route1
        if self.rules == Rule.Greedy_nn:
            self.logger.info("using greedy nn")

            sourcetest = 0
            targettest = len(self.data)+1

            res = greedy_nn(d, sourcetest, targettest, products_index_of_one_order_in_data)
            route1 = []
            path_copy = res['path'].copy()
            for i, p in enumerate(show_me_the_path(res['path'], path_list, products_index_of_one_order_in_data, maze1)):
                if i == 0:
                    part_res = (self.start_point,int(self.data[path_copy[1]-1][0]))
                    print(part_res)
                elif i == len(path_copy)-2:
                    part_res = (int(self.data[path_copy[i]-1][0]),self.end_point)
                else:
                    part_res = (int(self.data[path_copy[i]-1][0]),int(self.data[path_copy[i+1]-1][0]))
                route1.append("({}, {})".format(part_res,p))

                #route1.append("({},{})".format(p[0],p[1]))
            return route1

        self.logger.info("finish generating path")

    def load_data(self, path):
        self.data = self.dhandler.load_txt(path)
        for ind,d in enumerate(self.data):
            product = Products.Product(int(d[0]), d[1], d[2])
            self.products.append(product)
            self.id_to_ind_dict[d[0]] = ind+1

        pro_list = [[p.get_id(),p.x,p.y] for p in self.products]
        # draw_warehouse(pro_list,"data/path/warehouse.png")

        dot_list = []
        for p in pro_list:
            temp = [int(p[1]), int(p[2])]
            if temp not in dot_list:
                dot_list.append(temp)
        self.shelf_list = dot_list
        if not os.path.exists("data/path"):
            os.makedirs("data/path")
        draw_warehouse_html(self.shelf_list,"data/path/warehouse.html")

    def get_string_list_orders(self):
        orders=[]
        for order in self.orders:
            orders.append(order.to_string())
        return orders

