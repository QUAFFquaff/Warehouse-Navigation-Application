
import math

class worker:
    def __init__(self,id,psd,max_num = math.inf):
        self.__id = id
        self.__psd = psd
        self.__max_num = max_num

    # we may dont need all getter or setter, here just one example so i list almost all
    def get_psd(self):
        return self.__psd

    def set_psd(self,psd):
        self.__psd = psd

    def set_max_num(self,num):
        self.__max_num = num
    def get_max_num(self):
        return self.__max_num
    def get_id(self):
        return self.__id
    round(3)