import numpy as np

from algorithm.BruteForce import *

from DataHandler import DataHandler
from algorithm.MakeMatrix import MakeMatrix, brute_force

"""
generate random matrix for testing 
"""


file = DataHandler()
datatest = DataHandler.load_txt(file, '../data/qvBox-warehouse-data-f20-v01.txt')



order_listtest = [11,22,33,44,56]

ret = MakeMatrix(datatest,order_listtest)

print(ret['xmatrix'])
print(ret['ymatrix'])
d = ret['xmatrix'] + ret['ymatrix']
print(d)

res = brute_force(ret['xmatrix'],ret['ymatrix'],d,0,0, [1,2,3,4,5])
print(res)
