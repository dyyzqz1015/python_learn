# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSpinner.ui'
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 170, 54, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 112, 392, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditBookPrice = QtWidgets.QLabel(self.layoutWidget)
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.gridLayout.addWidget(self.lineEditBookPrice, 0, 0, 1, 1)
        self.lineEditBookPrice_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditBookPrice_2.setObjectName("lineEditBookPrice_2")
        self.gridLayout.addWidget(self.lineEditBookPrice_2, 0, 1, 1, 1)
        self.spinBoxBookQty = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.gridLayout.addWidget(self.spinBoxBookQty, 0, 2, 1, 1)
        self.lineEditBookAmount_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditBookAmount_2.setObjectName("lineEditBookAmount_2")
        self.gridLayout.addWidget(self.lineEditBookAmount_2, 0, 3, 1, 1)
        self.lineEditBookAmount = QtWidgets.QLabel(self.layoutWidget)
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.gridLayout.addWidget(self.lineEditBookAmount, 1, 0, 1, 1)
        self.lineEditSugarPrice = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.gridLayout.addWidget(self.lineEditSugarPrice, 1, 1, 1, 1)
        self.lineEditSugarAmount = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")
        self.gridLayout.addWidget(self.lineEditSugarAmount, 1, 3, 1, 1)
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.gridLayout.addWidget(self.doubleSpinBoxSugarWeight, 1, 2, 1, 1)
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
        self.lineEditBookPrice.setText(_translate("MainWindow", "Book Price"))
        self.lineEditBookAmount.setText(_translate("MainWindow", "Sugar Price"))

