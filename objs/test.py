#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/29/2020 23:33
# @Author  : Haoyu Lyu
# @File    : test.py
# @Software: PyCharm

import sys
import objs.WareHouse as WareHouse
wh = WareHouse.WareHouse()
wh.set_dhandler()
wh.load_data('../data/qvBox-warehouse-data-f20-v01.txt')
wh.add_order(3)
for o in wh.orders:
    for p in o.products:
        print(p.id)