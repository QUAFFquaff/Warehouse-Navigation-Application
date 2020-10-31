import numpy as np

import BruteForce
import algorithms
"""
generate random matrix for testing 
"""


xtemp = np.random.randint(1,6,(5,5))
xup = np.triu(xtemp)
x = xup + xup.T - np.diag(xtemp.diagonal())

ytemp = np.random.randint(1,6,(5,5))
yup = np.triu(ytemp)
y = yup + yup.T - np.diag(ytemp.diagonal())

d = x+y
print(d)




res = BruteForce.brute_force(x,y,d,0,0, [1,2,3,4])
print(res)
res = algorithms.dijkstra(0,d)
print(res)
