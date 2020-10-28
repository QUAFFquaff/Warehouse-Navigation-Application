#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/28/2020 9:51
# @Author  : Haoyu Lyu
# @File    : WareHouse.py
# @Software: PyCharm
import sys
from .DataHandler import DataHandler
from .Order import Order
from .Products import Product
import time
class WareHouse:
    def __init__(self,worker,orders = [], dhandler = None):

        self.worker = worker
        self.orders = orders
        self.dhandler = dhandler
        self.products = []

    def set_dhandler(self):
        self.dhandler =DataHandler()

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