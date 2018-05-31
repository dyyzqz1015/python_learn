#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/27 16:32
# @Author  : QinZai
# @File    : Dome.py
# @Software: PyCharm

import sys
from PyQt5 import QtCore, QtGui, uic,QtWidgets



qtCreatorFile = "mainwindow.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())