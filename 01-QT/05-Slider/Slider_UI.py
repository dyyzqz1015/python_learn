#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/26 16:47
# @Author  : QinZai
# @File    : Slider_UI.py
# @Software: PyCharm

import sys

from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QMessageBox
from PyQt5.QtCore import QCoreApplication
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)

qtCreatorFile = "form.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DomeUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        # lcd = QLCDNumber(self)    等同于，若已经画了界面，那么lcd=self.lcdNumber，lcdNumber是控件的名称
        # sld = QSlider(Qt.Horizontal, self)
        lcd=self.lcdNumber
        sld=self.horizontalSlider
        sld.valueChanged.connect(lcd.display)
        self.setWindowTitle('Signal and slot')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DomeUi()
    window.show()
    sys.exit(app.exec_())