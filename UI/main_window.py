# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Main_UI(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 30, 51, 41))
        self.label_image.setObjectName("label_image")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 490, 681, 81))
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
        self.label_graph.setGeometry(QtCore.QRect(120, 110, 491, 341))
        self.label_graph.setText("")
        self.label_graph.setObjectName("label_graph")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 120, 160, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView_orders = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView_orders.setObjectName("listView_orders")
        self.verticalLayout.addWidget(self.listView_orders)
        self.pushButton_add_order = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_add_order.setObjectName("pushButton_add_order")
        self.verticalLayout.addWidget(self.pushButton_add_order)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(680, 40, 108, 28))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(240, 30, 421, 41))
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
        self.pushButton_add_order.setText(_translate("MainWindow", "Add order"))
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

    def load_products(self):
        default_file="graph_data/graph.txt"
        filename, _ = QFileDialog.getOpenFileName(self, default_file)
        #TODO: generate graph image
        print('loading file location: ',filename)
        self.wh.load_data(filename)
        img_name = "data/images/graph_demo.png"
        img = QPixmap(img_name).scaled(self.label_graph.width(), self.label_graph.height())
        self.label_graph.setPixmap(img)

    def add_order(self):
        str="a->b->c"
        # TODO: get a order
        self.orders.append(str)
        self.orders_model.setStringList(self.orders)

    def finish_order(self):
        if self.clicked_order_index is None:
            QMessageBox.information(self, "Error", "Please select an order first！", QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.orders.pop(self.clicked_order_index)
            self.orders_model.setStringList(self.orders)
            self.clicked_order_index = None

    def set_profile_window(self,profile_window):
        self.profile=profile_window

    def set_warehouse(self,wh):
        self.warehouse=wh