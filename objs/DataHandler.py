
import utils.LoggerFactory as LF

class DataHandler:
    def __init__(self):
        pass

    def load_txt(self,path):
        logger=LF.get_logger(__name__)
        data = []
        logger.info('open file')
        with open(path, 'r') as f:
            f.readline()
            for line in f.readlines():
                data.append(list(map(float,line.split())))
        logger.info('read file complete')
        return data

    def load_orders(self,path):
        logger=LF.get_logger(__name__)
        data = []
        logger.info('open file')
        with open(path, 'r') as f:
            f.readline()
            for line in f.readlines():
                temp = line.split()
                temp = [t[:-1] if t[-1] == ',' else t for t in temp ]
                data.append(list(map(float,temp)))
        logger.info('read file complete')
        return data

    
# filename = '../data/qvBox-warehouse-orders-list-part01.txt'
# orders = DataHandler.load_orders(DataHandler,filename)
# print(orders)