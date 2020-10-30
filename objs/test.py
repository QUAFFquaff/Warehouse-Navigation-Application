#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/29/2020 23:33
# @Author  : Haoyu Lyu
# @File    : test.py
# @Software: PyCharm

import sys
from DataHandler import DataHandler
from WareHouse import WareHouse
wh = WareHouse()
wh.set_dhandler()
wh.load_data('../data/qvBox-warehouse-data-f20-v01.txt')
print(len(wh.products))