# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMouseClick.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 20, 691, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelPress = QtWidgets.QLabel(self.centralwidget)
        self.labelPress.setGeometry(QtCore.QRect(10, 60, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.labelPress.setFont(font)
        self.labelPress.setText("")
        self.labelPress.setObjectName("labelPress")
        self.labelRelease = QtWidgets.QLabel(self.centralwidget)
        self.labelRelease.setGeometry(QtCore.QRect(10, 100, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.labelRelease.setFont(font)
        self.labelRelease.setText("")
        self.labelRelease.setObjectName("labelRelease")
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
        self.label.setText(_translate("MainWindow", "Displays the x,y coordinates where mouse is pressed and released"))

