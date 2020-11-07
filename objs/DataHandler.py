
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

    
