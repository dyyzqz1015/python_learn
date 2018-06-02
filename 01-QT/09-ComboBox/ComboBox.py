#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/26 22:47
# @Author  : QinZai
# @File    : ComboBox.py
# @Software: PyCharm

import sys

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

        self.pushButton.clicked.connect(self.btnclick1)

        # b=self.comboBox.addItems(['1','2','3'])
        # a=self.lineEdit.setText(b)  # 获取单行输入框内的值
        # self.textEdit.setText(b) # 将单行输入框内的值，显示到多长输入框内
        # print(b)

    def btnclick1(self):
        # # a=self.lineEdit.text()  # 获取单行输入框内的值
        # # self.textEdit.setText(a) # 将单行输入框内的值，显示到多长输入框内
        b=self.comboBox.addItems(['1','2','3'])
        # a=self.lineEdit.text()  # 获取单行输入框内的内容
        a=self.lineEdit.setText('123')  # 获取单行输入框内的内容
        self.textEdit.setText(a) # 将单行输入框内的值，显示到多长输入框内
        # print(b)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DomeUi()
    window.show()
    sys.exit(app.exec_())