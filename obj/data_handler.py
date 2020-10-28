
class data_handler:

    def __init__(self):
        pass

    def load_txt(self):
        data = []
        txt_file = open("qvBox-warehouse-data-f20-v01.txt", "r")
        line0 = txt_file.readline()
        line = txt_file.readline()
        while line:
            data.append(line)
            line = txt_file.readline()
        txt_file.close()
        return data










