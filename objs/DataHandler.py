
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

    def save_orders(self,data,path,f):
        logger=LF.get_logger(__name__)
        logger.info('open file')
        for order in data:
            # logger.info('write order: ',order)
            f.write(str(order).replace('[','').replace(']','\n'))
        logger.info('write file complete')

    
# filename = '../data/unfinished_orders.txt'
# data = [[1,2],[3,4]]
# DataHandler.save_orders(DataHandler,data,filename)
