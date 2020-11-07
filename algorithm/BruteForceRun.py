
from objs.DataHandler import DataHandler
from algorithm.BruteForce import brute_force
from algorithm.MakeMatrix import make_matrix
from multiprocessing import Process, Manager
from algorithm.Direction import direction
from algorithm.GreedyNN import greedy_nn

##### INPUT ######

file = DataHandler()
datatest = DataHandler.load_txt(file, '../data/qvBox-warehouse-data-f20-v01.txt')

order_listtest = [17,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,19,20]

# [17,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,19,20]

start_point = (0.0, 0.0)
end_point = (0.0, 0.0)
sourcetest = 0
targettest = 25526

ret = make_matrix(datatest, start_point, end_point, order_listtest)

d = ret['xmatrix'] + ret['ymatrix']


#################################################################

res = greedy_nn(d, sourcetest, targettest, order_listtest)
print(res)



####### RUN BRUTE FORCE########

#### m here is same as res ###

manager = Manager()
m = manager.dict()
p1 = Process(target=brute_force, args=(m, d, sourcetest, targettest, order_listtest), name='process 1')
p1.start()
p1.join(timeout=4)
p1.terminate()
print(m)


##### SHOW DIRECTION #####

# route = direction(datatest, start_point, end_point, res)
# print(route)
#
# #### Write into txt #####
#
# with open('Route Direction Description.txt', 'a+') as ftest:
#     ftest.write('    NEW ORDER\n -----START-----\n')
#     for i in range(len(route)):
#         ftest.write(route[i])
#     ftest.write(' ------END------\n')
# #
