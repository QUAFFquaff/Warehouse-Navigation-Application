
import sys
from DataHandler import DataHandler
from Order import Order
from Products import Product
import time
class WareHouse:
    def __init__(self,worker = None ,orders = [], dhandler = None):

        self.worker = worker
        self.orders = orders
        self.dhandler = dhandler
        self.products = []
        self.rules = ""

    def set_dhandler(self):
        self.dhandler = DataHandler()

    def set_orders(self):
        self.orders = Order(time.time())

    def add_order(self,num):
        order = Order(time.time())
        order.init_products(num,self.products)
        self.orders.append(order)

    def generate_path(self):
        pass

    def set_rules(self):
        pass

    def load_data(self,path):
        data = self.dhandler.load_txt(path)
        for d in data:
            product = Product(int(d[0]),d[1],d[2])
            self.products.append(product)
    
    