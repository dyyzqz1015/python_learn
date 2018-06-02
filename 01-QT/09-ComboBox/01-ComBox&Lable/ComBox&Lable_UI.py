#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/26 23:46
# @Author  : QinZai
# @File    : ComBox&Lable_UI.py
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

        comBox=self.comboBox
        com_list=["MacOs","Ubuntu","Fedora","Arch","Gentoo"]
        comBox.addItems(com_list)

        comBox.activated[str].connect(self.onActivated)     #将选择后的内容连接到Label

    def onActivated(self,text):
        lb=self.label       #关联界面的label
        le=self.lineEdit
        te=self.textEdit
        lb.setText(text)        #将选择点击后的内容显示到label
        lb.adjustSize()         #自动调整显示的宽度

        le.setText(text)
        value=lb.text()         #获取Label的值
        te.setText(value)       #传递给多列文本当中







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DomeUi()
    window.show()
    sys.exit(app.exec_())