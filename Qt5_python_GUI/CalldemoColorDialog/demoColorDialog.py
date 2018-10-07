# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoColorDialog.ui'
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
        self.pushButtonColor = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonColor.setGeometry(QtCore.QRect(32, 42, 80, 23))
        self.pushButtonColor.setObjectName("pushButtonColor")
        self.labelColor = QtWidgets.QLabel(self.centralwidget)
        self.labelColor.setGeometry(QtCore.QRect(118, 42, 261, 16))
        self.labelColor.setObjectName("labelColor")
        self.frameColor = QtWidgets.QFrame(self.centralwidget)
        self.frameColor.setGeometry(QtCore.QRect(31, 88, 142, 40))
        self.frameColor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameColor.setObjectName("frameColor")
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
        self.pushButtonColor.setText(_translate("MainWindow", "Choose color"))
        self.labelColor.setText(_translate("MainWindow", "TextLabel"))

