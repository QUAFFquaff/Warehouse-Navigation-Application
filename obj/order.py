class order:

    def __init__(self, start_time):
        self.start_time = start_time
        self.finish_flag = False
        self.product_list = None
        self.finish_time = None

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
