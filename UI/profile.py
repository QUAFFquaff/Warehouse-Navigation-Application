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

class Profile_UI(QDialog):
    def setupUi(self, Profile):
        Profile.setObjectName("Profile")
        Profile.resize(788, 402)
        self.label_username = QtWidgets.QLabel(Profile)
        self.label_username.setGeometry(QtCore.QRect(120, 40, 101, 21))
        self.label_username.setObjectName("label_username")
        self.label_title = QtWidgets.QLabel(Profile)
        self.label_title.setGeometry(QtCore.QRect(260, 30, 311, 41))
        self.label_title.setObjectName("label_title")
        self.formLayoutWidget = QtWidgets.QWidget(Profile)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 100, 516, 143))
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
        self.comboBox_set_rules = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_set_rules.setObjectName("comboBox_set_rules")
        self.comboBox_set_rules.addItem("")
        self.comboBox_set_rules.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_set_rules)
        self.label_maximum_products = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_maximum_products.setObjectName("label_maximum_products")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_maximum_products)
        self.lineEdit_maximum_products = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_maximum_products.setObjectName("lineEdit_maximum_products")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_maximum_products)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Profile)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 270, 421, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_confirm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.horizontalLayout.addWidget(self.pushButton_confirm)
        self.pushButton_exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.label_image = QtWidgets.QLabel(Profile)
        self.label_image.setGeometry(QtCore.QRect(40, 30, 51, 41))
        self.label_image.setObjectName("label_image")
        self.radioButton_diagonal = QtWidgets.QRadioButton(Profile)
        self.radioButton_diagonal.setGeometry(QtCore.QRect(200, 250, 379, 20))
        self.radioButton_diagonal.setObjectName("radioButton_diagonal")

        self.retranslateUi(Profile)
        QtCore.QMetaObject.connectSlotsByName(Profile)

    def retranslateUi(self, Profile):
        _translate = QtCore.QCoreApplication.translate
        Profile.setWindowTitle(_translate("Profile", "Dialog"))
        self.label_username.setText(_translate("Profile", "alicebob"))
        self.label_title.setText(_translate("Profile", "Warehouse System Application"))
        self.label_change_password.setText(_translate("Profile", "Change Password"))
        self.label_confirm_password.setText(_translate("Profile", "Comfirm Password"))
        self.label_set_rules.setText(_translate("Profile", "Set Rules"))
        self.comboBox_set_rules.setItemText(0, _translate("Profile", "Branch_and_bound"))
        self.comboBox_set_rules.setItemText(1, _translate("Profile", "Greedy_nn"))
        self.label_maximum_products.setText(_translate("Profile", "Maximum Products"))
        self.pushButton_confirm.setText(_translate("Profile", "Confirm"))
        self.pushButton_exit.setText(_translate("Profile", "Exit"))
        self.label_image.setText(_translate("Profile", "Image"))
        self.radioButton_diagonal.setText(_translate("Profile", "allow_diagonal_movement"))

    # auto-generated code above
    # -------------------------------------------------

    # simple demo images
    def init(self):
        self.username=self.label_username.text()
        self.lineEdit_maximum_products.setText("1")
        self.add_event_listener()
        img_name = "data/images/head_img.png"
        img = QPixmap(img_name).scaled(self.label_image.width(), self.label_image.height())
        self.label_image.setPixmap(img)

    def add_event_listener(self):
        self.pushButton_exit.clicked.connect(self.reject)
        self.pushButton_confirm.clicked.connect(self.confirm)

    def confirm(self):
        params=self.get_params()
        self.warehouse.set_rules(params["rule"])
        self.warehouse.allow_diagonal_movement = self.radioButton_diagonal.isChecked()
        self.accept()

    # return a dict about the parameters in profile
    def get_params(self):
        params={}
        params["username"]=self.label_username.text()
        params["old_password"]=self.lineEdit_password_input1.text()
        params["new_password"] = self.lineEdit_password_input2.text()
        params["maximum_products"]=self.lineEdit_maximum_products.text()
        rule = self.comboBox_set_rules.currentText()
        if rule == "Branch_and_bound":
            params["rule"] = 0
        elif rule == "Greedy_nn":
            params["rule"] = 1
        return params

    def set_warehouse(self,wh):
        self.warehouse=wh
