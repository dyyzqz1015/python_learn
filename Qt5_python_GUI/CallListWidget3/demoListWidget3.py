# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.label.setObjectName("label")
        self.lineEditFoodItem = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(20, 150, 121, 23))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidgetSelectedItems = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetSelectedItems.setGeometry(QtCore.QRect(20, 180, 256, 192))
        self.listWidgetSelectedItems.setObjectName("listWidgetSelectedItems")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your favourite food"))
        self.pushButtonAdd.setText(_translate("MainWindow", "itemAdd to List"))

