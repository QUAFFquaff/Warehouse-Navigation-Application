# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Main_UI(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 30, 51, 21))
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
        self.label_username.setGeometry(QtCore.QRect(90, 30, 81, 21))
        self.label_username.setObjectName("label_username")
        self.label_graph = QtWidgets.QLabel(self.centralwidget)
        self.label_graph.setGeometry(QtCore.QRect(120, 110, 491, 341))
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
        self.pushButton_logout.setGeometry(QtCore.QRect(650, 40, 108, 28))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(250, 30, 311, 41))
        self.label_title.setObjectName("label_title")
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
        self.label_username.setText(_translate("MainWindow", "username"))
        self.label_graph.setText(_translate("MainWindow", "Displayed Image here"))
        self.pushButton_add_order.setText(_translate("MainWindow", "Add order"))
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))
        self.label_title.setText(_translate("MainWindow", "Warehouse System Application"))
