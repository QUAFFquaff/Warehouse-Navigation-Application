
import sys
import objs.DataHandler as DataHandler
import objs.Products as Products
import objs.Order as Order
import time
from enum import Enum
from algorithm.BruteForce import *
from algorithm.MakeMatrix import *
from algorithm.algorithms import *

Rule = Enum('Rule', ('Brute_force','Dijkstra'))
class WareHouse:
    def __init__(self,worker = None ,orders = [], dhandler = None):

        self.worker = worker
        self.orders = orders
        self.dhandler = dhandler
        self.products = []
        self.rules = Rule.Brute_force
        self.data = None

    def set_rules(self,num):
        if num == 0:
            self.rules = Rule.Brute_force
        elif num == 1:
            self.rules = Rule.Dijkstra

    def set_dhandler(self):
        self.dhandler = DataHandler.DataHandler()

    def set_orders(self):
        self.orders = Order.Order(time.time())

    def add_order(self,num):
        order = Order.Order(time.time())
        order.init_products(num,self.products)
        self.orders.append(order)

    def generate_path(self,order):

        order_listtest = [self.data.index(i) for i in order.products]
        pro_list = [[p.get_id(), p.x, p.y] for p in order.products]
        ret = MakeMatrix(self.data, order_listtest)
        print(ret)
        d = ret['xmatrix'] + ret['ymatrix']
        if self.rules == Rule.Brute_force:
            res = brute_force(ret['xmatrix'], ret['ymatrix'], d, 0, 0, [1, 2, 3, 4, 5])
            draw_png_graph(pro_list,res)
        pass


    def load_data(self,path):
        self.data = self.dhandler.load_txt(path)
        for d in self.data:
            product = Products.Product(int(d[0]),d[1],d[2])
            self.products.append(product)

    