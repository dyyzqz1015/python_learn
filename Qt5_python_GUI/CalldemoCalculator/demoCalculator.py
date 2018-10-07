# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 50, 322, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelFirstNumber = QtWidgets.QLabel(self.widget)
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.horizontalLayout_2.addWidget(self.labelFirstNumber)
        self.lineEditFirstNumber = QtWidgets.QLineEdit(self.widget)
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.horizontalLayout_2.addWidget(self.lineEditFirstNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelSecondNumber = QtWidgets.QLabel(self.widget)
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.horizontalLayout_3.addWidget(self.labelSecondNumber)
        self.lineEditSecondNumber = QtWidgets.QLineEdit(self.widget)
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.horizontalLayout_3.addWidget(self.lineEditSecondNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonPlus = QtWidgets.QPushButton(self.widget)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.horizontalLayout.addWidget(self.pushButtonPlus)
        self.pushButtonSubtract = QtWidgets.QPushButton(self.widget)
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.horizontalLayout.addWidget(self.pushButtonSubtract)
        self.pushButtonMultiply = QtWidgets.QPushButton(self.widget)
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.horizontalLayout.addWidget(self.pushButtonMultiply)
        self.pushButtonDivide = QtWidgets.QPushButton(self.widget)
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.horizontalLayout.addWidget(self.pushButtonDivide)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelResult = QtWidgets.QLabel(self.widget)
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
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
        self.labelFirstNumber.setText(_translate("MainWindow", "Enter first number"))
        self.labelSecondNumber.setText(_translate("MainWindow", "Enter second number"))
        self.pushButtonPlus.setText(_translate("MainWindow", "+"))
        self.pushButtonSubtract.setText(_translate("MainWindow", "-"))
        self.pushButtonMultiply.setText(_translate("MainWindow", "x"))
        self.pushButtonDivide.setText(_translate("MainWindow", "/"))
        self.labelResult.setText(_translate("MainWindow", "TextLabel"))

