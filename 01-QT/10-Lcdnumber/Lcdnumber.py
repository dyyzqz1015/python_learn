#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/27 15:20
# @Author  : QinZai
# @File    : Lcdnumber.py
# @Software: PyCharm

import sys
import time
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QMessageBox
from PyQt5.QtCore import QCoreApplication

qtCreatorFile = "form.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DomeUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        lcd=self.lcdNumber
        for i in range(5):

            lcd.display(i)
            time.sleep(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DomeUi()
    window.show()
    sys.exit(app.exec_())