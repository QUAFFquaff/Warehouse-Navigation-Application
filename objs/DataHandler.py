
class DataHandler:
    def __init__(self):
        pass

    def load_txt(self,path):
        data = []
        with open(path, 'r') as f:
            f.readline()
            for line in f.readlines():
                data.append(list(map(float,line.split())))
        return data

    
