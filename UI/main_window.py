from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
import re
import os
import utils.LoggerFactory as LF
logger=LF.get_logger(__name__)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from algorithm.algorithms import *
class Main_UI(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1296, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 30, 51, 41))
        self.label_image.setObjectName("label_image")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 680, 681, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_load_products = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_load_products.setObjectName("pushButton_load_products")
        self.horizontalLayout.addWidget(self.pushButton_load_products)
        self.pushButton_generate_path = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_generate_path.setObjectName("pushButton_generate_path")
        self.horizontalLayout.addWidget(self.pushButton_generate_path)
        self.pushButton_finish_order = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_finish_order.setObjectName("pushButton_finish_order")
        self.horizontalLayout.addWidget(self.pushButton_finish_order)
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(90, 40, 151, 21))
        self.label_username.setObjectName("label_username")
        self.label_graph = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.label_graph.setGeometry(QtCore.QRect(30, 210, 641, 441))
        self.label_graph.setObjectName("label_graph")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(880, 80, 391, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView_orders = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView_orders.setObjectName("listView_orders")
        self.verticalLayout.addWidget(self.listView_orders)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_products_id = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_products_id.setObjectName("label_products_id")
        self.horizontalLayout_4.addWidget(self.label_products_id)
        self.lineEdit_products_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_products_id.setObjectName("lineEdit_products_id")
        self.horizontalLayout_4.addWidget(self.lineEdit_products_id)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_add_order = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_add_order.setObjectName("pushButton_add_order")
        self.horizontalLayout_3.addWidget(self.pushButton_add_order)
        self.pushButton_add_orders_from_file = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_add_orders_from_file.setObjectName("pushButton_add_orders_from_file")
        self.horizontalLayout_3.addWidget(self.pushButton_add_orders_from_file)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(1070, 40, 191, 28))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(400, 30, 421, 41))
        self.label_title.setObjectName("label_title")
        self.pushButton_profile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile.setGeometry(QtCore.QRect(0, 90, 81, 41))
        self.pushButton_profile.setObjectName("pushButton_profile")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(720, 80, 151, 201))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_start_x = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_start_x.setObjectName("label_start_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_start_x)
        self.lineEdit_start_x = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_start_x.setObjectName("lineEdit_start_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_start_x)
        self.label_start_y = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_start_y.setObjectName("label_start_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_start_y)
        self.lineEdit_start_y = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_start_y.setObjectName("lineEdit_start_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_start_y)
        self.label_end_x = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_end_x.setObjectName("label_end_x")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_end_x)
        self.label_end_y = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_end_y.setObjectName("label_end_y")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_end_y)
        self.lineEdit_end_x = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_end_x.setObjectName("lineEdit_end_x")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_end_x)
        self.lineEdit_end_y = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_end_y.setObjectName("lineEdit_end_y")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_end_y)
        self.lineEdit_timeout = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_timeout.setObjectName("lineEdit_timeout")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_timeout)
        self.pushButton_set_start_and_end_point = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_set_start_and_end_point.setObjectName("pushButton_set_start_and_end_point")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton_set_start_and_end_point)
        self.label_timeout = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_timeout.setWordWrap(True)
        self.label_timeout.setObjectName("label_timeout")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_timeout)
        self.label_end_y_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_end_y_2.setGeometry(QtCore.QRect(30, 640, 661, 24))
        self.label_end_y_2.setObjectName("label_end_y_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 160, 21, 491))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_image.setText(_translate("MainWindow", "Image"))
        self.pushButton_load_products.setText(_translate("MainWindow", "Load Products"))
        self.pushButton_generate_path.setText(_translate("MainWindow", "Generate Path"))
        self.pushButton_finish_order.setText(_translate("MainWindow", "Finish Order"))
        self.label_username.setText(_translate("MainWindow", "alicebob"))
        self.label_products_id.setText(_translate("MainWindow", "Product(s) ID:"))
        self.pushButton_add_order.setText(_translate("MainWindow", "Add an order"))
        self.pushButton_add_orders_from_file.setText(_translate("MainWindow", "Add orders from file"))
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))
        self.label_title.setText(_translate("MainWindow", "                 Warehouse System Application"))
        self.pushButton_profile.setText(_translate("MainWindow", "Profile"))
        self.label_start_x.setText(_translate("MainWindow", "start x"))
        self.label_start_y.setText(_translate("MainWindow", "start y"))
        self.label_end_x.setText(_translate("MainWindow", "end x"))
        self.label_end_y.setText(_translate("MainWindow", "end y"))
        self.pushButton_set_start_and_end_point.setText(_translate("MainWindow", "set"))
        self.label_timeout.setText(_translate("MainWindow", "timeout"))
        self.label_end_y_2.setText(_translate("MainWindow", "------------------------------------------------------------------------------> x"))
        self.label.setText(_translate("MainWindow", "y ^ | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |"))

    # auto-generated code above
    # -------------------------------------------------

    # simple demo images
    def add_demo_images(self):
        img_name = "data/images/head_img.png"
        img = QPixmap(img_name).scaled(self.label_image.width(), self.label_image.height())
        self.label_image.setPixmap(img)

    def add_event_listener(self):
        self.pushButton_load_products.clicked.connect(self.load_products)
        self.pushButton_add_order.clicked.connect(self.add_order)
        self.pushButton_profile.clicked.connect(self.profile.exec_)
        self.pushButton_generate_path.clicked.connect(self.generate_path)
        self.pushButton_add_orders_from_file.clicked.connect(self.add_orders_from_file)
        self.pushButton_set_start_and_end_point.clicked.connect(self.set_start_and_end_point)

    def init(self):
        self.clicked_order_index = None
        self.add_demo_images()
        self.add_event_listener()
        self.orders = []
        self.orders_model=QStringListModel()
        self.listView_orders.setModel(self.orders_model)
        self.listView_orders.clicked.connect(self.order_clicked)
        self.pushButton_finish_order.clicked.connect(self.finish_order)
        self.lineEdit_start_x.setText("0")
        self.lineEdit_start_y.setText("0")
        self.lineEdit_end_x.setText("0")
        self.lineEdit_end_y.setText("0")
        self.lineEdit_timeout.setText("60")

    def order_clicked(self,index):
        self.clicked_order_index = index.row()
        # TODO display image

    def load_products(self):
        default_file="graph_data/graph.txt"
        filename, _ = QFileDialog.getOpenFileName(self, default_file)
        if filename is None or filename=="":
            filename="data/qvBox-warehouse-data-f20-v01.txt"
        if not filename.endswith(".txt"):
            QMessageBox.information(self, "error", "The file has to be a txt file", QMessageBox.Yes, QMessageBox.Yes)
            return
        logger.info('loading file location: {}'.format(filename))
        try:
            self.warehouse.load_data(str(filename))
        except Exception() as e:
            QMessageBox.information(self, "error", "exception", QMessageBox.Yes, QMessageBox.Yes)
            return
        path = os.path.join(os.getcwd(),"data","path","warehouse.html").replace("\\","/")
        # self.label_graph.load(QUrl("D:/program/python/Warehouse-Navigation-Application/data/path/file_name.html"))
        self.label_graph.load(QUrl("file:///{}".format(path)))
        # img_name = "data/path/warehouse.png"
        # img = QPixmap(img_name).scaled(self.label_graph.width(), self.label_graph.height())
        # self.label_graph.setPixmap(img)


    def add_orders_from_file(self):
        if self.warehouse.data is None:
            QMessageBox.information(self, "error", "no data loaded", QMessageBox.Yes,
                                    QMessageBox.Yes)
            return
        default_file = "data/qvBox-warehouse-orders-list-part01.txt"
        filename, _ = QFileDialog.getOpenFileName(self, default_file)
        if filename is None or filename=="":
            filename="data/qvBox-warehouse-orders-list-part01.txt"
        if not filename.endswith(".txt"):
            QMessageBox.information(self, "error", "The file has to be a txt file", QMessageBox.Yes, QMessageBox.Yes)
            return
        logger.info('loading file location: {}'.format(filename))
        try:
            self.warehouse.load_orders(str(filename))
            self.orders=self.warehouse.get_string_list_orders()
            self.orders_model.setStringList(self.orders)
        except Exception() as e:
            QMessageBox.information(self, "error", "exception", QMessageBox.Yes, QMessageBox.Yes)
            return
        QMessageBox.information(self, "Info", "success", QMessageBox.Yes, QMessageBox.Yes)

    def add_order(self):
        if self.warehouse.data is None:
            QMessageBox.information(self, "error", "no data loaded", QMessageBox.Yes,
                                    QMessageBox.Yes)
            return
        products_id=self.lineEdit_products_id.text()
        if products_id == "":
            self.order_len = 3
            self.warehouse.add_order(self.order_len)
        else:
            if not re.match("(\d+)(,\d+)*",products_id):
                QMessageBox.information(self, "Error", "invalid format! should be like: 123,456,789", QMessageBox.Yes, QMessageBox.Yes)
                return
            try:
                self.warehouse.add_order(3,products_id.split(","))
            except:
                QMessageBox.information(self, "Error", "exception", QMessageBox.Yes, QMessageBox.Yes)
                return
        products = self.warehouse.orders[-1].products
        l = []
        for p in products:
            l.append(str(p.get_id()))
        self.orders.append(", ".join(l))
        self.orders_model.setStringList(self.orders)
        pro_list = [[p.get_id(),p.x,p.y] for p in products]
        img_name = "data/path/dot.png"
        draw_png_dot_graph(pro_list,img_name)
        img_name = "data/path/dot.html"
        draw_dots_html(pro_list,img_name)
        path = os.path.join(os.getcwd(),"data","path","dot.html").replace("\\","/")
        self.label_graph.load(QUrl("file:///{}".format(path)))

    def get_order_index(self):
        if self.clicked_order_index is None:
            QMessageBox.information(self, "Error", "Please select an order first！", QMessageBox.Yes, QMessageBox.Yes)
            return None
        else:
            index=self.clicked_order_index
            self.clicked_order_index = None
            return index

    def finish_order(self):
        index=self.get_order_index()
        if index is not None:
            self.orders.pop(index)
            self.warehouse.orders.pop(index)
            self.warehouse.products_index_of_one_order_in_data.pop(index)
            self.orders_model.setStringList(self.orders)

    def set_profile_window(self,profile_window):
        self.profile=profile_window

    def set_warehouse(self,wh):
        self.warehouse=wh

    def generate_path(self):
        if self.warehouse.data is None:
            QMessageBox.information(self, "error", "no data loaded", QMessageBox.Yes,
                                    QMessageBox.Yes)
            return
        index = self.get_order_index()
        if index is not None:
            logger.info('send order {}'.format(self.orders[index]))
            route=self.warehouse.generate_path(self.warehouse.orders[index],index)

            path = os.path.join(os.getcwd(), "data", "path", "path.html").replace("\\", "/")
            self.label_graph.load(QUrl("file:///{}".format(path)))
            QMessageBox.information(self, "Info", " ".join(route), QMessageBox.Yes, QMessageBox.Yes)

    def set_start_and_end_point(self):
        start_x = self.lineEdit_start_x.text()
        start_y = self.lineEdit_start_y.text()
        end_x = self.lineEdit_end_x.text()
        end_y = self.lineEdit_end_y.text()
        timeout = self.lineEdit_timeout.text()

        reg="(\d+)"
        float_reg="\d+(\.\d+)?"

        if not re.fullmatch(reg,start_x) or not re.fullmatch(reg,start_y) or not re.fullmatch(reg,end_x) or not re.fullmatch(reg,end_y) or not re.fullmatch(float_reg,timeout):
            QMessageBox.information(self, "Error", "Wrong input format, numbers only!", QMessageBox.Yes, QMessageBox.Yes)
            return
        try:
            self.warehouse.start_point=(int(start_x),int(start_y))
            self.warehouse.end_point=(int(end_x),int(end_y))
            self.warehouse.timeout=float(timeout)
            logger.info("setting start point to ({}, {})".format(start_x,start_y))
            logger.info("setting end point to ({}, {})".format(end_x,end_y))
        except Exception() as e:
            QMessageBox.information(self, "Exception", e, QMessageBox.Yes, QMessageBox.Yes)
            return
        QMessageBox.information(self, "Info", "success", QMessageBox.Yes, QMessageBox.Yes)

