#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/29/2020 23:33
# @Author  : Haoyu Lyu
# @File    : test.py
# @Software: PyCharm

import sys
from WareHouse import *
wh = WareHouse()
wh.set_dhandler()
wh.load_data('F:/Users/lenovo/Documents/!ProgramZone/Python/EECS221c/Warehouse-Navigation-Application/data/qvBox-warehouse-data-f20-v01.txt')
wh.add_order(3)
for o in wh.orders:
    for p in o.products:
        print(p.id)