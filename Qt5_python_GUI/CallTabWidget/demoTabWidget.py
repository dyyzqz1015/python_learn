# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoTabWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 381, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.AfterCurrentPage = QtWidgets.QWidget()
        self.AfterCurrentPage.setObjectName("AfterCurrentPage")
        self.layoutWidget = QtWidgets.QWidget(self.AfterCurrentPage)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.tabWidget.addTab(self.AfterCurrentPage, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.radioButton = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton.setGeometry(QtCore.QRect(40, 50, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 80, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 120, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 150, 261, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.DeliveryAddress = QtWidgets.QWidget()
        self.DeliveryAddress.setObjectName("DeliveryAddress")
        self.widget = QtWidgets.QWidget(self.DeliveryAddress)
        self.widget.setGeometry(QtCore.QRect(10, 20, 86, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget1 = QtWidgets.QWidget(self.DeliveryAddress)
        self.widget1.setGeometry(QtCore.QRect(110, 20, 135, 171))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_3.addWidget(self.lineEdit_6)
        self.tabWidget.addTab(self.DeliveryAddress, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add to Cart"))
        self.checkBox_4.setText(_translate("MainWindow", "Cell Phone $150"))
        self.checkBox_3.setText(_translate("MainWindow", "Laptop $500"))
        self.checkBox_2.setText(_translate("MainWindow", "Camera $250"))
        self.checkBox.setText(_translate("MainWindow", "Shoes $200"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AfterCurrentPage), _translate("MainWindow", "Product Listing"))
        self.radioButton.setText(_translate("MainWindow", "Debit Card"))
        self.radioButton_2.setText(_translate("MainWindow", "Credit Card"))
        self.radioButton_3.setText(_translate("MainWindow", "Net Banking"))
        self.radioButton_4.setText(_translate("MainWindow", "Cash On Delivery"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Payment Method"))
        self.label_6.setText(_translate("MainWindow", "Address1 "))
        self.label_5.setText(_translate("MainWindow", "Address2"))
        self.label_4.setText(_translate("MainWindow", "State"))
        self.label_3.setText(_translate("MainWindow", "Country"))
        self.label_2.setText(_translate("MainWindow", "Code"))
        self.label.setText(_translate("MainWindow", "Contact Number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DeliveryAddress), _translate("MainWindow", "Delivery Address"))
