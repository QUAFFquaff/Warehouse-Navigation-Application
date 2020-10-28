# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
import os

class Profile_UI(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 402)
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setGeometry(QtCore.QRect(120, 40, 71, 21))
        self.label_username.setObjectName("label_username")
        self.label_image = QtWidgets.QLabel(Dialog)
        self.label_image.setGeometry(QtCore.QRect(50, 40, 51, 21))
        self.label_image.setObjectName("label_image")
        self.pushButton_logout = QtWidgets.QPushButton(Dialog)
        self.pushButton_logout.setGeometry(QtCore.QRect(530, 40, 108, 28))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(260, 30, 311, 41))
        self.label_title.setObjectName("label_title")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 100, 431, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_change_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_change_password.setObjectName("label_change_password")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_change_password)
        self.lineEdit_password_input1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_password_input1.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password_input1.setText("")
        self.lineEdit_password_input1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_input1.setObjectName("lineEdit_password_input1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password_input1)
        self.label_confirm_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_confirm_password)
        self.lineEdit_password_input2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_password_input2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password_input2.setText("")
        self.lineEdit_password_input2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_input2.setObjectName("lineEdit_password_input2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password_input2)
        self.label_set_rules = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_set_rules.setObjectName("label_set_rules")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_set_rules)
        self.label_maximum_products = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_maximum_products.setObjectName("label_maximum_products")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_maximum_products)
        self.comboBox_set_rules = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_set_rules.setObjectName("comboBox_set_rules")
        self.comboBox_set_rules.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_set_rules)
        self.lineEdit_maximum_products = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_maximum_products.setObjectName("lineEdit_maximum_products")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_maximum_products)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 270, 421, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_username.setText(_translate("Dialog", "username"))
        self.label_image.setText(_translate("Dialog", "Image"))
        self.pushButton_logout.setText(_translate("Dialog", "Logout"))
        self.label_title.setText(_translate("Dialog", "Warehouse System Application"))
        self.label_change_password.setText(_translate("Dialog", "Change Password"))
        self.label_confirm_password.setText(_translate("Dialog", "Comfirm Password"))
        self.label_set_rules.setText(_translate("Dialog", "Set Rules"))
        self.label_maximum_products.setText(_translate("Dialog", "Maximum Products"))
        self.comboBox_set_rules.setItemText(0, _translate("Dialog", "Dijkstra"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))

    # auto-generated code above
    # -------------------------------------------------

    # simple demo images
    def init(self):
        img_name = "UI/images/head_img.png"
        img = QPixmap(img_name).scaled(self.label_image.width(), self.label_image.height())
        self.label_image.setPixmap(img)
