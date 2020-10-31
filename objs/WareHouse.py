
import sys
from DataHandler import *
from Order import *
from Products import *
import time
from enum import Enum
from algorithm.MakeMatrix import *

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
        self.dhandler = DataHandler()

    def set_orders(self):
        self.orders = Order(time.time())

    def add_order(self,num):
        order = Order(time.time())
        order.init_products(num,self.products)
        self.orders.append(order)

    def generate_path(self,order):

        if self.rules == Rule.Brute_force:
            order_listtest = [self.data.index(i) for i in order.products]
            ret = MakeMatrix(self.data, order_listtest)
            print(ret)
        pass


    def load_data(self,path):
        self.data = self.dhandler.load_txt(path)
        for d in self.data:
            product = Product(int(d[0]),d[1],d[2])
            self.products.append(product)

    