from PyQt5 import QtCore, QtGui, QtWidgets
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
        MainWindow.resize(1226, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 30, 51, 41))
        self.label_image.setObjectName("label_image")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 620, 681, 81))
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
        self.label_graph = QtWidgets.QLabel(self.centralwidget)
        self.label_graph.setGeometry(QtCore.QRect(150, 110, 611, 451))
        self.label_graph.setText("")
        self.label_graph.setObjectName("label_graph")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 100, 351, 571))
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
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(927, 40, 191, 28))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(400, 30, 421, 41))
        self.label_title.setObjectName("label_title")
        self.pushButton_profile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile.setGeometry(QtCore.QRect(0, 90, 81, 41))
        self.pushButton_profile.setObjectName("pushButton_profile")
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
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))
        self.label_title.setText(_translate("MainWindow", "                 Warehouse System Application"))
        self.pushButton_profile.setText(_translate("MainWindow", "Profile"))
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

    def init(self):
        self.clicked_order_index = None
        self.add_demo_images()
        self.add_event_listener()
        self.orders = []
        self.orders_model=QStringListModel()
        self.listView_orders.setModel(self.orders_model)
        self.listView_orders.clicked.connect(self.order_clicked)
        self.pushButton_finish_order.clicked.connect(self.finish_order)

    def order_clicked(self,index):
        self.clicked_order_index = index.row()
        # TODO display image

    def load_products(self):
        default_file="graph_data/graph.txt"
        filename, _ = QFileDialog.getOpenFileName(self, default_file)
        if filename is None or filename=="":
            filename="data/qvBox-warehouse-data-f20-v01.txt"
        #TODO: generate graph image

        logger.info('loading file location: {}'.format(filename))
        self.warehose.load_data(str(filename))

        #img_name = "data/images/graph_demo.png"
        #img = QPixmap(img_name).scaled(self.label_graph.width(), self.label_graph.height())
        #self.label_graph.setPixmap(img)

    def add_order(self):
        products_id=self.lineEdit_products_id.text()
        if  products_id == "":
            self.order_len = 3
            self.warehouse.add_order(self.order_len)
        else:
            if not re.match("(\d+)(,\d+)*",products_id):
                QMessageBox.information(self, "Error", "invalid format! should be like: 123,456,789", QMessageBox.Yes, QMessageBox.Yes)
                return
            self.warehouse.add_order(3,products_id.split(","))
        products = self.warehouse.orders[-1].products
        l = []
        for p in products:
            l.append(str(p.get_id()))
        self.orders.append(", ".join(l))
        self.orders_model.setStringList(self.orders)
        pro_list = [[p.get_id(),p.x,p.y] for p in products]
        img_name = "data/path/dot.png"
        draw_png_dot_graph(pro_list,img_name)
        img = QPixmap(img_name).scaled(self.label_graph.width(), self.label_graph.height())
        self.label_graph.setPixmap(img)

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
            self.orders_model.setStringList(self.orders)

    def set_profile_window(self,profile_window):
        self.profile=profile_window

    def set_warehouse(self,wh):
        self.warehouse=wh

    def generate_path(self):
        index = self.get_order_index()
        if index is not None:
            # TODO: display image here

            logger.info('send order {}'.format(self.orders[index]))
            route=self.warehouse.generate_path(self.warehouse.orders[index],index)

            img_name = "data/path/path.png"
            img = QPixmap(img_name).scaled(self.label_graph.width(), self.label_graph.height())
            self.label_graph.setPixmap(img)
            QMessageBox.information(self, "Info", " ".join(route), QMessageBox.Yes, QMessageBox.Yes)
            #self.label.setText("This graph shows the path from the starting area to the return area. The worker will follow the path to get products")