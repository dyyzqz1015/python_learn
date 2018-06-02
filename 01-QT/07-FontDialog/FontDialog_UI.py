#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 01-QT
# @Time    : 2018/5/26 18:13
# @Author  : QinZai
# @File    : FontDialog_UI.py
# @Software: PyCharm

import sys

from PyQt5 import uic, QtCore, QtWidgets

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QFontDialog, QApplication)
import sys

qtCreatorFile = "form.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DomeUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        btn=self.pushButton
        # btn.setSizePolicy(QSizePolicy.Fixed,
        #               QSizePolicy.Fixed)

        btn.clicked.connect(self.showDialog)

    def showDialog(self):
        lbl = self.label
        font, ok = QFontDialog.getFont()
        if ok:
            lbl.setFont(font)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DomeUi()
    window.show()
    sys.exit(app.exec_())