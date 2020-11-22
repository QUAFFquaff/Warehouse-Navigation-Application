import sys
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

from objs.DataHandler import *

Rule = Enum('Rule', ('Brute_force', 'Dijkstra'))
import utils.LoggerFactory as LF
from multiprocessing import Process, Manager

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

    def set_rules(self, num):
        if num == 0:
            self.rules = Rule.Brute_force
        elif num == 1:
            self.rules = Rule.Dijkstra

    def set_dhandler(self):
        self.dhandler = DataHandler()

    def set_orders(self):
        self.orders = Order.Order(time.time())

    def add_order(self, num, p_list=None):
        if not p_list:
            order = Order.Order(time.time())
            ids = order.init_products(num, self.products)
            self.order_listtest.append(ids)
            self.orders.append(order)
            self.products_index_of_one_order_in_data.append(ids)
            return ids
        else:
            order = Order.Order(time.time())
            p_list = list(map(int,p_list))
            for i in range(len(p_list)):
                if self.id_to_ind_dict.get(p_list[i]) is None:
                    logger.error("Product id {} not found!".format(p_list[i]))
                    raise Exception("Product id not found!")
                p_list[i]=self.id_to_ind_dict[p_list[i]]
            ids = order.add_products(p_list,self.products)
            self.order_listtest.append(ids)
            self.products_index_of_one_order_in_data.append(ids)
            self.orders.append(order)
            return ids

    def load_orders(self,filename):
        logger.info("loading orders from {}".format(filename))
        pass

    def generate_path(self,order,index):
        '''

        :param order:
        :param index: index of the order in all orders
        :return:
        '''
        products_index_of_one_order_in_data = self.products_index_of_one_order_in_data[index]
        logger.info("products_index_of_one_order_in_data: {}".format(products_index_of_one_order_in_data))

        pro_list = [[p.get_id(), p.x, p.y] for p in order.products]
     #############
        #ret = make_matrix(self.data, self.start_point, self.end_point, products_index_of_one_order_in_data)

        #d = ret['xmatrix'] + ret['ymatrix']
     #############
        maze1 = make_maze(self.data)
        d = make_astar_matrix(self.data, maze1, self.start_point, self.end_point, products_index_of_one_order_in_data)

        if self.rules == Rule.Brute_force:
            self.logger.info("using brute force")
            temp = [i + 1 for i in range(len(pro_list))]

            ##################
            sourcetest = 0
            targettest = 25526
            start_point = (0,0)
            end_point = (0,0)
            manager = Manager()
            m = manager.dict()
            p1 = Process(target=brute_force, args=(m, d, sourcetest, targettest, products_index_of_one_order_in_data),
                         name='process 1')
            p1.start()
            p1.join(timeout=60)
            p1.terminate()
            logger.info("m['path']: {}".format(m['path']))
            route = direction(self.data, start_point, end_point, m)
            ############################
            self.logger.info("brute force result(path): {}".format(m["path"]))
            self.logger.info("draw png graph")
            self.logger.info("pro_list: {}".format(pro_list))
            draw_png_graph(pro_list, m['path'])
            self.logger.info("finish generating path")
            return route
        self.logger.info("finish generating path")

    def load_data(self, path):
        self.data = self.dhandler.load_txt(path)
        for ind,d in enumerate(self.data):
            product = Products.Product(int(d[0]), d[1], d[2])
            self.products.append(product)
            self.id_to_ind_dict[d[0]] = ind+1

        pro_list = [[p.get_id(),p.x,p.y] for p in self.products]
        draw_warehouse(pro_list,"data/path/warehouse.png")

    def get_string_list_orders(self):
        orders=[]
        for order in self.orders:
            orders.append(order.to_string())
        return orders