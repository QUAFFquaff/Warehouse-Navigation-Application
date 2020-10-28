#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/28/2020 9:45
# @Author  : Haoyu Lyu
# @File    : DataHandler.py
# @Software: PyCharm
class DataHandler:
    def __init__(self):
        pass

    def load_txt(self,path):
        data = []
        with open(path, 'r') as f:
            f.readline()
            for line in f.readlines():
                data.append(list(map(int,line.split())))
        return data

    