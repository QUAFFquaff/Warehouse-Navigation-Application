
import sys
from DataHandler import DataHandler
from Order import Order
from Products import Product
import time
class WareHouse:
    def __init__(self,worker,orders = [], dhandler = None):

        self.worker = worker
        self.orders = orders
        self.dhandler = dhandler
        self.products = []

    def set_dhandler(self):
        self.dhandler = DataHandler()

    def set_orders(self):
        self.orders = Order(time.time())

    def create_orders(self,num):
        order = Order(time.time())
        order.init_products(num,self.products,999)
        self.orders.append(order)

    def generate_path(self):
        pass

    def set_rules(self):
        pass

    def load_data(self,path):
        data = self.dhandler.loadTxt(path)
        for d in data:
            product = Product(d[0],d[1],d[2])
            self.products.append(product)
    
    