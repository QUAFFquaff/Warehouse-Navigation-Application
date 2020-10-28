#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/28/2020 9:37
# @Author  : Haoyu Lyu
# @File    : Order.py
# @Software: PyCharm
import math
import random
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
class Order:
    def __init__(self,products, start_time, finish_time=-1):
        self.products = products
        self.start_time = start_time
        self.finish_time = finish_time

    def init_products(self,num,all_products,max=math.inf):
        ids = random_int_list(0,len(all_products),num)
        self.products = all_products[ids]



