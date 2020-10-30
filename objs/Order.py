
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
    def __init__(self, start_time, products = [], finish_time=-1):
        self.products = products
        self.start_time = start_time
        self.finish_time = finish_time

        self.start_time = start_time
        self.finish_flag = False
        self.product_list = None
        self.finish_time = None

    def init_products(self,num,all_products,max=math.inf):
        ids = random_int_list(0,len(all_products),num)
        self.products = all_products[ids]



    def set_product_list(self, product_list):
        self.product_list = product_list

    def set_finish_time(self, finish_time):
        self.finish_time = finish_time

    # retrieve order info #
    def order_info(self):
        if not self.finish_flag:
            print('This order has %d items, created at %s, Unfinished' % (len(self.product_list), self.start_time))
        else:
            print('This order has %d items, created at %s, finished at %s' % (len(self.product_list), self.start_time,
                                                                              self.finish_time))

