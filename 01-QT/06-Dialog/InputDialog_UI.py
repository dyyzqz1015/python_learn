#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/26 17:28
# @Author  : QinZai
# @File    : InputDialog_UI.py
# @Software: PyCharm



from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
import sys
qtCreatorFile = "Dome.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DomeUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        btn=self.pushButton
        # le=self.lineEdit
        a='aa'

        btn.clicked.connect(self.showDialog)

    def showDialog(self):
        le = self.lineEdit

        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            # self.lineEdit.setText(str(text))
            le.setText(str(text))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DomeUi()
    window.show()
    sys.exit(app.exec_())