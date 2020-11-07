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

            ids = p_list
            self.order_listtest.append(ids)
            self.products_index_of_one_order_in_data.append(ids)
            self.orders.append(order)
            return ids

    def generate_path(self,order,index):
        '''

        :param order:
        :param index: index of the order in all orders
        :return:
        '''
        products_index_of_one_order_in_data = self.products_index_of_one_order_in_data[index]
        products_index_of_one_order_in_data = [10790, 21432, 643]
        print(products_index_of_one_order_in_data)

        pro_list = [[p.get_id(), p.x, p.y] for p in order.products]
        ret = make_matrix(self.data, self.start_point, self.end_point, products_index_of_one_order_in_data)

        d = ret['xmatrix'] + ret['ymatrix']

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
            p1.join(timeout=4)
            p1.terminate()
            print(m['path'])
            route = direction(self.data, start_point, end_point, m)
            ############################
            self.logger.info("brute force result(path): {}".format(m["path"]))
            self.logger.info("draw png graph")
            draw_png_graph(pro_list, m['path'])
            self.logger.info("finish generating path")
            return route
        self.logger.info("finish generating path")

    def load_data(self, path):
        self.data = self.dhandler.load_txt(path)
        for d in self.data:
            product = Products.Product(int(d[0]), d[1], d[2])
            self.products.append(product)

